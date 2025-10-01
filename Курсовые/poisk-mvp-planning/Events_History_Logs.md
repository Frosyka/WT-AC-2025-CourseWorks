# Events / History / Logs

| Слой | Назначение | Где хранится | Триггер | Пример записи | Потребитель |
|------|------------|--------------|---------|---------------|-------------|
| Events | Хронология действий группы/зон | events table | POST event | ZONE_PASSED zone=z2 | Координатор, отчёт |
| History | Изменения статусов заявки | history table | PATCH status | NEW→ACTIVE | Пользователь, аудит |
| Logs | Техконтекст и ошибки | log sink/file | Система / middleware | 403 role=volunteer | Разработчик |
