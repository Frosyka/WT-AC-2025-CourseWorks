#!/usr/bin/env python3
"""Read check_result.json and comment + label the PR on failure.

Features added:
- Logging (stdout)
- Avoid duplicate labels (checks existing labels first)
- Avoid duplicate bot comments (searches comments for identical body or marker)
- Short and long templates for comments
"""
import os
import json
import sys
import logging
from typing import Any, List
import urllib.request
import urllib.error


LOG = logging.getLogger('comment_and_label')
LOG.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
LOG.addHandler(handler)


SHORT_TEMPLATE = '⚠️ Обнаружены изменения вне вашей разрешённой директории. Пожалуйста, перенесите изменения в свою папку.'

LONG_TEMPLATE = (
    '⚠️ Обнаружены изменения вне вашей разрешённой директории.\n\n'
    'Разрешённая директория: **{allowed}**\n\n'
    'Изменённые файлы, которые нужно перенести:\n{files}\n\n'
    'Инструкция: перенесите ваши файлы в указанную папку и создайте новый PR. Если вы считаете, что изменения вне папки обоснованы, ответьте на этот комментарий и преподаватель рассмотрит ваш случай.'
)

MULTI_TASK_TEMPLATE = (
    '⚠️ В одном pull request обнаружены изменения сразу по нескольким заданиям: {tasks}.\n\n'
    'Пожалуйста, разделите каждое задание в отдельный PR (например, task_01 — один PR, task_02 — другой).'
)


def get_issue_comments(repo: str, pr_number: str, headers: dict) -> List[dict]:
    url = f'https://api.github.com/repos/{repo}/issues/{pr_number}/comments'
    req = urllib.request.Request(url, headers=headers, method='GET')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status != 200:
                LOG.warning('Failed to fetch comments: %s', resp.status)
                return []
            data = resp.read().decode('utf-8')
            return json.loads(data)
    except urllib.error.HTTPError as e:
        LOG.warning('Failed to fetch comments: %s %s', e.code, e.read().decode('utf-8', 'ignore'))
        return []


def get_issue_labels(repo: str, pr_number: str, headers: dict) -> List[str]:
    url = f'https://api.github.com/repos/{repo}/issues/{pr_number}/labels'
    req = urllib.request.Request(url, headers=headers, method='GET')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            if resp.status != 200:
                LOG.warning('Failed to fetch labels: %s', resp.status)
                return []
            data = json.loads(resp.read().decode('utf-8'))
            return [lbl.get('name') for lbl in data if isinstance(lbl, dict)]
    except urllib.error.HTTPError as e:
        LOG.warning('Failed to fetch labels: %s %s', e.code, e.read().decode('utf-8', 'ignore'))
        return []


def post_comment(repo: str, pr_number: str, headers: dict, body: str) -> int:
    url = f'https://api.github.com/repos/{repo}/issues/{pr_number}/comments'
    data = json.dumps({'body': body}).encode('utf-8')
    hdrs = {**headers, 'Content-Type': 'application/json'}
    req = urllib.request.Request(url, headers=hdrs, data=data, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            LOG.info('post_comment status=%s', resp.status)
            return resp.status
    except urllib.error.HTTPError as e:
        LOG.info('post_comment status=%s', e.code)
        return e.code


def add_label(repo: str, pr_number: str, headers: dict, label: str) -> int:
    url = f'https://api.github.com/repos/{repo}/issues/{pr_number}/labels'
    data = json.dumps([label]).encode('utf-8')
    hdrs = {**headers, 'Content-Type': 'application/json'}
    req = urllib.request.Request(url, headers=hdrs, data=data, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            LOG.info('add_label status=%s', resp.status)
            return resp.status
    except urllib.error.HTTPError as e:
        LOG.info('add_label status=%s', e.code)
        return e.code


def close_pull_request(repo: str, pr_number: str, headers: dict) -> int:
    url = f'https://api.github.com/repos/{repo}/issues/{pr_number}'
    data = json.dumps({'state': 'closed'}).encode('utf-8')
    hdrs = {**headers, 'Content-Type': 'application/json'}
    req = urllib.request.Request(url, headers=hdrs, data=data, method='PATCH')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            LOG.info('close_pr status=%s', resp.status)
            return resp.status
    except urllib.error.HTTPError as e:
        LOG.info('close_pr status=%s', e.code)
        return e.code


def main() -> int:
    repo = os.environ.get('REPO')
    pr = os.environ.get('PR_NUMBER')
    token = os.environ.get('GITHUB_TOKEN')
    path = os.environ.get('CHECK_RESULT_PATH', '.github/check_result.json')

    if not repo or not pr or not token:
        LOG.error('Missing required environment variables (REPO, PR_NUMBER, GITHUB_TOKEN)')
        return 1

    if not os.path.exists(path):
        LOG.info('No result file at %s', path)
        return 0

    data: Any = json.load(open(path, encoding='utf-8'))
    exit_code = int(data.get('exit_code', 1))
    if exit_code not in (2, 3, 4):
        LOG.info('No failure detected (exit_code=%s), nothing to do', exit_code)
        return 0

    violations = data.get('violations', [])
    author = data.get('author', 'unknown')
    allowed = data.get('allowed', 'unknown')
    tasks = data.get('tasks', [])

    # Prepare body
    if exit_code == 3:
        body = f"⚠️ Невозможно сопоставить пользователя **{author}** с `students/students.csv`. Пожалуйста, проверьте вручную."
    elif exit_code == 4:
        tasks_list = ', '.join(f'`{t}`' for t in tasks[:10])
        body = MULTI_TASK_TEMPLATE.format(tasks=tasks_list or '—')
    else:
        files_list = '\n'.join(f'- {v}' for v in violations[:20])
        body = LONG_TEMPLATE.format(allowed=allowed, files=files_list)

    headers = {'Authorization': f'token {token}', 'Accept': 'application/vnd.github.v3+json'}

    # Avoid duplicate comments: look for an existing bot comment with marker and update it
    marker = '<!-- student-dir-checker -->'
    marked_body = marker + '\n' + body
    comments = get_issue_comments(repo, pr, headers)
    existing_id = None
    for c in comments:
        if marker in (c.get('body') or ''):
            existing_id = c.get('id')
            LOG.info('Found existing bot comment id=%s, will update', existing_id)
            break

    if existing_id:
        # update comment via PATCH
        url = f'https://api.github.com/repos/{repo}/issues/comments/{existing_id}'
        data = json.dumps({'body': marked_body}).encode('utf-8')
        hdrs = {**headers, 'Content-Type': 'application/json'}
        req = urllib.request.Request(url, headers=hdrs, data=data, method='PATCH')
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                LOG.info('update_comment status=%s', resp.status)
        except urllib.error.HTTPError as e:
            LOG.info('update_comment status=%s', e.code)
    else:
        post_comment(repo, pr, headers, marked_body)

    # Avoid duplicate label
    existing_labels = get_issue_labels(repo, pr, headers)
    label = 'Wrong dir'
    if label in existing_labels:
        LOG.info('Label %s already present — skipping', label)
    else:
        add_label(repo, pr, headers, label)

    close_pull_request(repo, pr, headers)

    return 0


if __name__ == '__main__':
    sys.exit(main())
