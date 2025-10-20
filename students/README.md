# Students submissions

Размещайте курсовые проекты здесь, организованные по студентам.

Структура (для курсовых):
- students/<ваш_идентификатор>/{apps,packages,docs,infra,k8s,.env.example,docker-compose.yml,...}
  - Рекомендуемый каркас смотрите в README репозитория (раздел «Структура размещения студенческих проектов»).

Как начать:
- Скопируйте пример [students/TestovTestTestovich](../students/TestovTestTestovich) (или создайте по аналогии) в `students/<ваш_идентификатор>`.
- Положите код серверной и клиентской части в `apps/` (web/server), общий код — в `packages/`.
- Документацию и архитектуру — в `docs/`.

Перед Pull Request: обязательно синхронизируйте свою ветку с основной (`upstream/main`). Инструкция — аналогична лабораторным (см. репозиторий WT-AC-2025).

## Запрос на смену темы/архитектуры (Task 00)

- Поместите заявку по шаблону в students/<NameLatin>/task_00/REQUEST_change_topic.md (пример каталога: [./VashchukAnatoliy](./VashchukAnatoliy)).
- Подробная инструкция: [docs/INSTRUCTION_change_topic_architecture.md](../docs/INSTRUCTION_change_topic_architecture.md).
- Создайте PR из форка с заголовком `[TASK_00][<NameLatin>] Request change topic/architecture`.
