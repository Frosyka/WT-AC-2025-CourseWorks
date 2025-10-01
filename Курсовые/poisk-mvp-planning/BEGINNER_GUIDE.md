# Beginner Guide (Poisk MVP)

> Навигация: [Воркбук](./workbook/Воркбук.md) · [WBS](./WBS_Детализация.md) · [Glossary](./Glossary.md)
>
> Raw: [Воркбук](./workbook/Воркбук.md) | [WBS](./WBS_Детализация.md) | [Glossary](./Glossary.md)

Краткий маршрут для студента: с чего начать, что обязательно, а что можно отложить.

## 1. Цель за 5 минут

Понять: «Мы показываем путь от регистрации заявки до отчёта о работе группы на местности».

## 2. Минимальный набор файлов для старта

1. `workbook/Воркбук.md` (прочитать разделы 1–3).
2. `access/Матрица_прав.md` (понять роли и кто что может).
3. `api/Валидаторы.md` (какие поля обязательны у заявки).
4. `WBS_Детализация.md` (только свой эпик — см. ниже).
5. Релиз текущего этапа: `workbook/Релизы/R1_...` или `R2_...` по календарю группы.

## 3. Как выбрать задачу

1. Открой `WBS_Детализация.md`.
2. Найди эпик (A–G) соответствующий твоему поднаправлению (пример: backend CRUD — A / C; права — B; прогресс — D; НФ — E; демо — F; бонусы — G).
3. Возьми самую верхнюю невыполненную задачу без незакрытых зависимостей (столбец DEP).
4. Создай ветку `feature/<ID-задачи>`.

## 4. Минимальный рабочий сквозной сценарий

1. Создать заявку (POST /api/requests).
2. Получить список (GET /api/requests).
3. Добавить зоны (POST /api/requests/{id}/zones).
4. Создать группу (POST /api/groups) и связать с заявкой.
5. Зафиксировать событие (POST /api/groups/{id}/events).
6. Посчитать покрытие / прогресс (GET /api/requests/{id}/coverage).
7. Сформировать отчёт (GET /api/requests/{id}/report).

## 5. Формат события (Event) — черновой JSON

```json
{
  "id": "evt_123",
  "groupId": "g_1",
  "type": "ZONE_PASSED", // START, STOP, ZONE_PASSED, NOTE
  "zoneId": "z_2",
  "ts": "2025-10-01T18:45:00Z",
  "actor": "user_5",
  "comment": "Проверена опушка"
}
```

## 6. История vs События vs Логи

| Слой | Что хранит | Пример | Кто читает |
|------|------------|--------|------------|
| История (history) | Изменения статусов заявки | status: NEW→ACTIVE | Пользователь, координатор |
| События (events) | Бизнес-акты группы/зон | ZONE_PASSED, START | Координатор, отчёт |
| Логи (logs) | Тех. записи, ошибки, 403 | auth denied role=volunteer | Разработчик/админ |

## 7. Типовые статусы заявки (итерация 1)

NEW → IN_PROGRESS → GROUP_ASSIGNED → ACTIVE → COMPLETED *(или CANCELLED)*

## 8. Checklist перед PR

- [ ] Название ветки `feature/<ID>`
- [ ] Есть curl или httpie пример запроса/ответа
- [ ] Ошибки (400/403/404) обработаны
- [ ] Обновлён связанный раздел документации
- [ ] Нет лишних отладочных конструкций

## 9. Как понять, что делать дальше?

- Если зависимость блокирует: перейди на задачу из другого эпика без зависимостей.
- Если неясно поле/формат — ищи в `R1_Модель_данных_API.md` или `R2_Детализация_API.md`.
- Если не хватает термина — посмотри `Glossary.md`.

## 10. FAQ (кратко)

Q: Нужно ли сразу делать метрики?  
A: Нет, это эпик G (R4).

Q: Где источник истины по задачам?  
A: `WBS_Детализация.md`.

Q: Как добавить новое поле в заявку?  
A: Обнови миграцию/модель + валидации + описание в R1/R2.

## 11. Инструменты для сокращения рутины

Ниже — практические тулзы и приёмы, которые экономят время. Бери точечно под текущий этап (R1–R4), не ставь всё сразу.

### 11.1 R1 (Модель данных, базовый REST)

- ER / схема: dbdiagram.io, QuickDBD — хранить текстовую схему в `docs/schema/er.txt`.
- Генерация миграций: Prisma (schema → миграции) или Sqitch (чистый SQL).
- Генераторы кода: Plop.js / Hygen (шаблон контроллер + сервис + тест).
- Моки/данные: json-server для прототипа, @faker-js/faker для сидов (`npm run seed`).
- REST тестирование: VS Code REST Client (`api/requests.http`) или Bruno (хранится в git).
- Форматирование и стиль: Prettier + ESLint + husky + lint-staged.

### 11.2 R2 (Роли, детализация API, история)

- Спека → типы: OpenAPI + openapi-typescript → `types/api.d.ts`.
- Валидация: Zod схемы + генерация OpenAPI (openapi-zod) как единый источник.
- Генерация клиента: openapi-generator-cli (папка `clients/ts/`).
- Документация: Redoc CLI (статический `docs/public/api.html`).
- Матрица прав автопроверка: кастомный тест + Casl (если динамика) или простые enum проверки.
- Контроль зависимостей слоёв: dependency-cruiser (правило «UI не импортирует infra»).

### 11.3 Асинхронность и устойчивость

- Повторы: p-retry / async-retry для обёртки внешних вызовов.
- Очереди (если появится фон): BullMQ (Redis) для задач (пересчёт отчётов, уведомления).

### 11.4 R3 (НФ требования, отчёты, качество)

- Тесты API: Jest + Supertest.
- Изоляция сетевых вызовов (позже фронт): MSW или Nock.
- Покрытие: c8 (ESM) или Istanbul.
- Статический анализ: eslint-plugin-security, depcheck (неиспользуемые пакеты).
- Производительность: autocannon (baseline latency), Clinic.js (узкие места).
- Логирование: pino + pino-http + correlation id (middleware) + pino-pretty (dev только).
- Метрики: prom-client → `/metrics` (дальше Prometheus + Grafana docker-compose при необходимости).
- Лицензии: license-checker.
- Changelog: conventional-changelog-cli + commitlint.

### 11.5 R4 (Бонусы, экспорт, оптимизация)

- Экспорт: json2csv / fast-csv, pdfkit (при необходимости PDF).
- Кэширование: lru-cache (in-memory) или Redis + ioredis.
- Rate limiting: express-rate-limit + express-slow-down.
- Трассировка: OpenTelemetry SDK + Jaeger (docker all-in-one) локально.
- API Drift тесты: Schemathesis (fuzz) + Dredd (консистентность реализации со спекой).
- Контейнер безопасность: Trivy (fs/image scan).
- SQL оптимизация: EXPLAIN (ANALYZE) скрипты + pgBadger анализ логов.
- Bundle анализ (фронт): source-map-explorer, Lighthouse CI.

### 11.6 Productivity (горизонтальные вещи)

- Task runner: npm scripts / Just / Taskfile — унифицировать команды.
- Генерация диаграмм: Mermaid CLI или Kroki (CI рендер PNG/SVG).
- Орфография документации: cspell (добавить доменные термины).
- Markdown автофикс: markdownlint-cli2 --fix в pre-commit.
- ADR: adr-tools (`docs/adr/0001-используем-openapi.md`).
- Live reload: nodemon или tsx watch (если TypeScript).
- Env управление: dotenv-flow / direnv.
- Диаграммы зависимостей: madge → `graph.png`.

### 11.7 Быстрые победы (<= 1 час)

1. Husky + lint-staged: блокируем мусор до commit.
2. `api/requests.http`: мгновенный smoke для CRUD.
3. `openapi/poisk.yaml` + генерация типов.
4. pino + X-Request-Id middleware.
5. `npm run benchmark` (autocannon) — фиксируем baseline.

### 11.8 Мини дорожная карта внедрения

- Неделя 1: Prettier/ESLint/husky + REST Client + pino.
- Неделя 2: OpenAPI skeleton + openapi-typescript + первые Supertest.
- Неделя 3: prom-client + rate-limit + autocannon baseline.
- Неделя 4: Redoc build + Schemathesis smoke + Trivy.
- Неделя 5+: OpenTelemetry + Grafana (если есть смысл).

### 11.9 Ритуалы для устойчивости

- Новая сущность → сначала схема в OpenAPI/Zod → генерация типов → реализация.
- Новый endpoint → запись в `api/requests.http` → ручной test → автотест.
- Существенное решение → ADR файл.
- Производительность упала >20% от baseline → создаём задачу в WBS.

> Подсказка: не внедряйте инструмент без явной окупаемости (время * частота). Если пользу сложно сформулировать одной строкой — отложите.

Удачи! Начинай с малого — первая рабочая цепочка важнее количества кода.

