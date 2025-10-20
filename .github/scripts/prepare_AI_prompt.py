"""Prepare AI prompt for grading a student's work.

Usage: python prepare_AI_prompt.py --student <StudentDirectoryName> --task <taskN>

For курсовые проекты we don't have per-task rubrics like labs; we assemble a generic
prompt using README rubric and focus on student folder students/<NameLatin>/task_XX.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load_file(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--student', required=True)
    ap.add_argument('--task', required=True, help='task_XX or number')
    args = ap.parse_args(argv)

    student = re.sub(r'[^A-Za-z0-9_-]', '', args.student)
    m = re.search(r'(\d+)', args.task)
    task_folder = f'task_{int(m.group(1)):02d}' if m else 'task_01'

    readme = load_file(ROOT / 'README.md')

    system_message = (
        "Ты строгий проверяющий курсовых проектов по веб-технологиям. Оценивай строго по критериям из README, не выходи за рамки шаблона, не добавляй воды."
    )

    prompt = [
        "[System message для AI]:",
        system_message,
        "[Рекомендация: temperature=0.3 для консистентности]",
        "",
        "Оцени курсовой проект студента.",
        f"Смотреть файлы только в папке: ('students/{student}/{task_folder}').",
        f"Проверять только работу в папке: '{task_folder}'.",
        "Игнорируй бинарные и медиа-файлы (изображения/архивы/видео/аудио).",
        "Оцени по критериям из раздела 'Критерии оценивания' README данного репозитория. Если критерии не найдены — укажи, что критерии недоступны.",
        "Выводи строго в формате:\nкритерии: NNN / XXX\nИтого: NNN / 100",
        "Кратко предложи до 2 улучшений (по одному предложению).",
    ]

    print("\n".join(prompt))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
