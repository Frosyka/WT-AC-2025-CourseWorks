# Курсовые работы — Веб-Технологии (4 курс)

Этот раздел содержит материалы для выполнения и проверки курсовых работ по дисциплине «Веб-Технологии». Все задания опираются на темы лабораторных работ (вёрстка, DOM/JS, HTTP и кэширование, REST, Node/Express, БД и авторизация, React, качество/деплой/Docker/CI/CD).

## Обязательный минимум (MVP)
- Репозиторий Git (публичный или приватный с доступом преподавателю).
- Full‑stack: клиент (SPA/SSR) + сервер (REST API) + БД.
- Аутентификация (вход/регистрация на JWT) и базовая авторизация (минимум: user, admin).
- Валидация данных на клиенте и сервере; обработка ошибок с человекочитаемыми сообщениями.
- Нефункциональные минимум: a11y (базово) , CORS и helmet, логирование, пагинация/фильтры по необходимости.
- Контейнеризация (желательно, но не обязательно): Docker для server и БД; Docker Compose — для локальной разработки.
#TODO a11y расрыть юолее детально

Примечание: Kubernetes, тесты и API‑документация не требуются для базовой оценки — они учитываются как бонусы.

## Опционально за доп. баллы (бонусы, суммарно до +50)
- Документация API: OpenAPI/Swagger или коллекция запросов (HTTP/REST Client, Postman): +8
- Тестирование: unit/integration (сервер) и/или e2e (Playwright): +15
- Деплой в Kubernetes (k8s/ манифесты: Deployments, Services, Ingress, ConfigMap/Secret, PVC; пробы/ресурсы; HPA — по желанию): +15
- CI (GitHub Actions/GitLab CI): линтинг + тесты + сборка образов: +7
- Наблюдаемость/оптимизация: структурированные логи, базовые метрики/аннотации Prometheus, кэш Redis, WebSocket/Web Push/PWA‑офлайн (по задаче): до +5

## Рекомендованный стек (можно согласовывать альтернативы)
- Frontend: TypeScript + React (Vite/Next.js) или Vue/Svelte.
- Backend: Node.js + Express/NestJS/Fastify; ORM/ODM: Prisma/TypeORM/Mongoose.
- БД: PostgreSQL (рекомендуется) или MongoDB; кэш: Redis (по необходимости).
- Инструменты: ESLint/Prettier, Jest/Vitest/Playwright, Swagger/OpenAPI, Docker, Kubernetes (kubectl, Kustomize/Helm — опционально).

## Критерии оценивания
База (до 50) + бонусы (до +50) = максимум 100 баллов.
- База (50):
  - Архитектура и полнота требований: 15
  - Качество кода и типизация: 10
  - Клиент (UI/UX, маршрутизация, состояние): 12
  - Сервер (REST, безопасность, валидация): 10
  - Данные и миграции/сидинг: 3
- Бонусы (до +50): см. раздел «Опционально за доп. баллы».

#TODO рассмотреть штрафы
## Порядок работы
1) Выберите тему.
2) Соберите MVP (обязательный минимум).
3) По желанию добавьте бонусы: документация API, тесты, Kubernetes, CI и др.
4) Подготовьте защиту: сценарий демо + данные.


## Рекомендуемая структура репозитория (best practice)

```
root/
  README.md
  .editorconfig
  .gitignore
  .env.example            # образец переменных окружения (без секретов)
  package.json            # monorepo/workspaces (опционально)
  pnpm-workspace.yaml     # или npm/yarn workspaces (опционально)
  docker-compose.yml      # локальная разработка (по желанию)
  docs/
    architecture.md       # схема, решения по архитектуре
    api.md                # OpenAPI ссылка/снимки (если делаете бонус с документацией)
  .github/
    workflows/
      ci.yml              # линтинг, тесты, сборка, образы (если делаете бонус с CI)
  .vscode/
    settings.json
    extensions.json
  apps/
    server/
      src/
      package.json
      Dockerfile
      openapi.yaml        # спецификация API (если делаете бонус с документацией)
      prisma/ или migrations/   # ORM/миграции БД
    web/
      src/
      package.json
      Dockerfile
  packages/               # опционально: общие библиотеки (ui, utils)
    ui/
    utils/
  infra/
    db/
      migrations/
      seeds/
    scripts/
      migrate.ts
      seed.ts
  k8s/                    # опционально: если делаете бонус с Kubernetes
    base/
      namespace.yaml
      server-deployment.yaml
      server-service.yaml
      web-deployment.yaml
      web-service.yaml
      ingress.yaml
      configmap.yaml
      secret.yaml         # секреты через env → Secret (не хранить реальные ключи)
      postgres-statefulset.yaml
      postgres-pvc.yaml
    overlays/
      dev/
        kustomization.yaml
      prod/
        kustomization.yaml
```

Короткие примечания:
- apps/: разделяем web и server; удобно для CI, версионирования и Docker.
- packages/: общий код (компоненты/UI, утилиты, схемы валидаторов) — по необходимости.
- k8s/: храните манифесты только если берёте бонус за Kubernetes.
- docs/api.md и openapi.yaml — если берёте бонус за документацию API.
- .github/workflows — если берёте бонус за CI.
- .env.example: образец переменных; секреты — только через Kubernetes Secrets.
