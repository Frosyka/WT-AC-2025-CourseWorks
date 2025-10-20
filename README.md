# Курсовые работы — Веб-Технологии (4 курс)

Этот раздел содержит материалы для выполнения и проверки курсовых работ по дисциплине «Веб-Технологии». Все задания опираются на темы лабораторных работ (вёрстка, DOM/JS, HTTP и кэширование, REST, Node/Express, БД и авторизация, React, качество/деплой/Docker/CI/CD).

## Обязательный минимум (MVP)

- Репозиторий Git (публичный или приватный с доступом преподавателю).
- Full‑stack: клиент (SPA/SSR) + сервер (REST API) + БД.
- Аутентификация (вход/регистрация на JWT) и базовая авторизация (минимум: user, admin).
- Валидация данных на клиенте и сервере; обработка ошибок с человекочитаемыми сообщениями.
- Нефункциональные минимум: a11y (базово), CORS и helmet, логирование, пагинация/фильтры по необходимости.
- Контейнеризация (желательно, но не обязательно): Docker для server и БД; Docker Compose — для локальной разработки.

<!-- TODO: детализировать требования по a11y -->

Примечание: Kubernetes, тесты и API‑документация не требуются для базовой оценки — они учитываются как бонусы.

## Задание #1 (R1): Документация проекта

Каждый студент должен подготовить R1-документацию по своему варианту.

- Шаблон и инструкции: [tasks/task_01_R1/README.md](./tasks/task_01_R1/README.md)
- Шаблоны файлов для копирования: [tasks/task_01_R1/template](./tasks/task_01_R1/template/)
- Сдача: [students/<NameLatin>/task_01/](./students/) (внутри положить файлы `R1_*.md` из шаблона, заполненные под свой вариант)

R1 включает: маршруты, роли/действия, матрицу прав, модели данных и API, ERD, WBS и карточки задач с критериями приёмки.

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

<!-- TODO: добавить описание возможных штрафов -->

## Порядок работы

1. Выберите тему.
2. Соберите MVP (обязательный минимум).
3. (Опционально) Добавьте бонусы: документация API, тесты, Kubernetes, CI и др.
4. Подготовьте защиту: сценарий демо + данные.

## Структура размещения студенческих проектов

Каждый студент создаёт свой рабочий каркас внутри каталога [students/<student_id>/](./students/).
Пример: [students/TestovTestTestovich](./students/TestovTestTestovich):

```text

  test_id/
    apps/
      server/
        src/
          index.ts
          routes/
          modules/
          middleware/
          lib/
        prisma/
        migrations/
        openapi.yaml
        package.json
        Dockerfile
      web/
        src/
          main.tsx
          App.tsx
          pages/
          components/
          features/
          entities/
          shared/
        index.html
        package.json
        Dockerfile
    packages/
      ui/
      utils/
    docs/
      architecture.md
      api.md
    infra/
      scripts/
      db/
    k8s/
      base/
      overlays/
        dev/
        prod/
    .env.example
    docker-compose.yml
    pnpm-workspace.yaml
    package.json
```

Короткие примечания:

- apps/: разделяем web и server; удобно для CI, версионирования и Docker.
- packages/: общий код (компоненты/UI, утилиты, схемы валидаторов) — по необходимости.
- k8s/: храните манифесты только если берёте бонус за Kubernetes.
- docs/api.md и openapi.yaml — если берёте бонус за документацию API.
- .github/workflows — если берёте бонус за CI.
- .env.example: образец переменных; секреты — только через Kubernetes Secrets.

### Шаги для нового студента

## Успеваемость
<!-- STUDENTS_TABLE_START -->

| Вариант | Group | № | sub | Name | NameLatin | Directory | Github Username | #0 | #1 | #2 | #3 | #4 | Rating |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 20 | АС-63 | 1 | 2 | Ващук Анатолий | VashchukAnatoliy | [dir](./students/VashchukAnatoliy) | [skevet-avramuk](https://github.com/skevet-avramuk) |  |  |  |  |  |  |
| 23 | АС-63 | 2 | 1 | Выржемковский Даниил | VyrzhemkovskiyDaniil | [dir](./students/VyrzhemkovskiyDaniil) | [r0mb123](https://github.com/r0mb123) |  |  |  |  |  |  |
| 24 | АС-63 | 3 | 1 | Грицук Дмитрий | GritsukDmitriy | [dir](./students/GritsukDmitriy) | [llayyz](https://github.com/llayyz) |  |  |  |  |  |  |
| 32 | АС-63 | 4 | 1 | Грицук Павел | GritsukPavel | [dir](./students/GritsukPavel) | [momo-kitsune](https://github.com/momo-kitsune) |  |  |  |  |  |  |
| 27 | АС-63 | 5 | 1 | Казаренко Павел | KazarenkoPavel | [dir](./students/KazarenkoPavel) | [Catsker](https://github.com/Catsker) |  |  |  |  |  |  |
| 19 | АС-63 | 6 | 1 | Карпеш Никита | KarpeshNikita | [dir](./students/KarpeshNikita) | [Frosyka](https://github.com/Frosyka) |  |  |  |  |  |  |
| 11 | АС-63 | 7 | 1 | Козлович Антон | KozlovichAnton | [dir](./students/KozlovichAnton) | [Anton777kozlovich](https://github.com/Anton777kozlovich) |  |  |  |  |  |  |
| 15 | АС-63 | 8 | 1 | Козловская Анна | KozlovskayaAnna | [dir](./students/KozlovskayaAnna) | [annkrq](https://github.com/annkrq) |  |  |  |  |  |  |
| 21 | АС-63 | 9 | 1 | Колодич Максим | KolodichMaksim | [dir](./students/KolodichMaksim) | [proxladno](https://github.com/proxladno) |  |  |  |  |  |  |
| 29 | АС-63 | 10 | 1 | Крагель Алина | KragelAlina | [dir](./students/KragelAlina) | [Alina529](https://github.com/Alina529) |  |  |  |  |  |  |
| 44 | АС-63 | 11 | 2 | Куликович Иван | KulikovichIvan | [dir](./students/KulikovichIvan) | [teenage717](https://github.com/teenage717) |  |  |  |  |  |  |
| 34 | АС-63 | 12 | 2 | Кульбеда Кирилл | KulbedaKirill | [dir](./students/KulbedaKirill) | [fr0ogi](https://github.com/fr0ogi) |  |  |  |  |  |  |
| 13 | АС-63 | 13 | 2 | Кухарчук Илья | KukharchukIlya | [dir](./students/KukharchukIlya) | [IlyaKukharchuk](https://github.com/IlyaKukharchuk) |  |  |  |  |  |  |
| 40 | АС-63 | 14 | 1 | Логинов Глеб | LoginovGleb | [dir](./students/LoginovGleb) | [gleb7499](https://github.com/gleb7499) |  |  |  |  |  |  |
| 18 | АС-63 | 15 | 2 | Мороз Евгений | MorozEvgeniy | [dir](./students/MorozEvgeniy) | [EugeneFr0st](https://github.com/EugeneFr0st) |  |  |  |  |  |  |
| 3 | АС-63 | 16 | 2 | Никифоров Александр | NikiforovAleksandr | [dir](./students/NikiforovAleksandr) | [woQhy](https://github.com/woQhy) |  |  |  |  |  |  |
|   | АС-63 | 17 | 2 | Поплавский Владислав | PoplavskiyVladislav | [dir](./students/PoplavskiyVladislav) | [ImRaDeR1](https://github.com/ImRaDeR1) |  |  |  |  |  |  |
| 26 | АС-63 | 18 | 2 | Савко Павел | SavkoPavel | [dir](./students/SavkoPavel) | [1nsirius](https://github.com/1nsirius) |  |  |  |  |  |  |
| 25 | АС-63 | 19 | 1 | Соколова Маргарита | SokolovaMargarita | [dir](./students/SokolovaMargarita) | [Ritkas33395553](https://github.com/Ritkas33395553) |  |  |  |  |  |  |
| 38 | АС-63 | 20 | 2 | Стельмашук Иван | StelmashukIvan | [dir](./students/StelmashukIvan) | [KulibinI](https://github.com/KulibinI) |  |  |  |  |  |  |
| 39 | АС-63 | 21 | 2 | Тунчик Антон | TunchikAnton | [dir](./students/TunchikAnton) | [Stis25](https://github.com/Stis25) |  |  |  |  |  |  |
| 16 | АС-63 | 22 | 2 | Филипчук Дмитрий | FilipchukDmitriy | [dir](./students/FilipchukDmitriy) | [kuddel11](https://github.com/kuddel11) |  |  |  |  |  |  |
| 9 | АС-63 | 23 | 2 | Ярмола Александр | YarmolaAleksandr | [dir](./students/YarmolaAleksandr) | [alexsandro007](https://github.com/alexsandro007) |  |  |  |  |  |  |
| 8 | АС-63 | 24 | 2 | Ярмолович Александр | YarmolovichAleksandr | [dir](./students/YarmolovichAleksandr) | [yarmolov](https://github.com/yarmolov) |  |  |  |  |  |  |
| 37 | АС-64 | 1 | 1 | Белаш Александр | BelashAleksandr | [dir](./students/BelashAleksandr) | [went2smoke](https://github.com/went2smoke) |  |  |  |  |  |  |
| 7 | АС-64 | 2 | 1 | Брызгалов Юрий | BryzgalovYuriy | [dir](./students/BryzgalovYuriy) | [Gena-Cidarmyan](https://github.com/Gena-Cidarmyan) |  |  |  |  |  |  |
| 12 | АС-64 | 3 | 1 | Будник Анна | BudnikAnna | [dir](./students/BudnikAnna) | [annettebb](https://github.com/annettebb) |  |  |  |  |  |  |
| 33 | АС-64 | 4 | 1 | Булавский Андрей | BulavskiyAndrey | [dir](./students/BulavskiyAndrey) | [andrei1910bl](https://github.com/andrei1910bl) |  |  |  |  |  |  |
| 43 | АС-64 | 5 | 2 | Бурак Илья | BurakIlya | [dir](./students/BurakIlya) | [burakillya](https://github.com/burakillya) |  |  |  |  |  |  |
| 17 | АС-64 | 6 | 1 | Горкавчук Никита | GorkavchukNikita | [dir](./students/GorkavchukNikita) | [Exage](https://github.com/Exage) |  |  |  |  |  |  |
| 4 | АС-64 | 7 | 1 | Евкович Андрей | EvkovichAndrey | [dir](./students/EvkovichAndrey) | [Andrei21005](https://github.com/Andrei21005) |  |  |  |  |  |  |
| 14 | АС-64 | 8 | 1 | Иванюк Иван | IvanyukIvan | [dir](./students/IvanyukIvan) | [JonF1re](https://github.com/JonF1re) |  |  |  |  |  |  |
| 36 | АС-64 | 9 | 1 | Игнаткевич Кирилл | IgnatkevichKirill | [dir](./students/IgnatkevichKirill) | [pyrokekw](https://github.com/pyrokekw) |  |  |  |  |  |  |
| 22 | АС-64 | 10 | 1 | Кашпир Дмитрий | KashpirDmitriy | [dir](./students/KashpirDmitriy) | [Dima-kashpir](https://github.com/Dima-kashpir) |  |  |  |  |  |  |
| 30 | АС-64 | 11 | 1 | Котковец Кирилл | KotkovetsKirill | [dir](./students/KotkovetsKirill) | [Kirill-Kotkovets](https://github.com/Kirill-Kotkovets) |  |  |  |  |  |  |
| 6 | АС-64 | 12 | 2 | Кужир Владислав | KuzhirVladislav | [dir](./students/KuzhirVladislav) | [XD-cods](https://github.com/XD-cods) |  |  |  |  |  |  |
| 35 | АС-64 | 13 | 2 | Немирович Дмитрий | NemirovichDmitriy | [dir](./students/NemirovichDmitriy) | [goryachiy-ugolek](https://github.com/goryachiy-ugolek) |  |  |  |  |  |  |
| 2 | АС-64 | 14 | 2 | Попов Алексей | PopovAleksey | [dir](./students/PopovAleksey) | [LexusxdsD](https://github.com/LexusxdsD) |  |  |  |  |  |  |
| 31 | АС-64 | 15 | 2 | Рабченя Максим | RabchenyaMaksim | [dir](./students/RabchenyaMaksim) | [benwer9q](https://github.com/benwer9q) |  |  |  |  |  |  |
| 28 | АС-64 | 16 | 1 | Ровнейко Захар | RovneykoZakhar | [dir](./students/RovneykoZakhar) | [Zaharihnio](https://github.com/Zaharihnio) |  |  |  |  |  |  |
| 41 | АС-64 | 17 | 2 | Смердина Анастасия | SmerdinaAnastasiya | [dir](./students/SmerdinaAnastasiya) | [KotyaLapka](https://github.com/KotyaLapka) |  |  |  |  |  |  |
| 1 | АС-64 | 18 | 2 | Хомич Виталий | KhomichVitaliy | [dir](./students/KhomichVitaliy) | [VitlyaNB](https://github.com/VitlyaNB) |  |  |  |  |  |  |
| 43 | Test | 0 | 0 | Тестов Тест Тестович | TestovTestTestovich | [dir](./students/TestovTestTestovich) |  |  |  |  |  |  |  |
| 23 | АС-63 | 2 | 1 | Выржемковский Даниил | VyrzhemkovskiyDaniil | [dir](./students/VyrzhemkovskiyDaniil) | [r0mb123](https://github.com/r0mb123) |  |  |  |  |  |  |
| 24 | АС-63 | 3 | 1 | Грицук Дмитрий | GritsukDmitriy | [dir](./students/GritsukDmitriy) | [llayyz](https://github.com/llayyz) |  |  |  |  |  |  |
| 32 | АС-63 | 4 | 1 | Грицук Павел | GritsukPavel | [dir](./students/GritsukPavel) | [momo-kitsune](https://github.com/momo-kitsune) |  |  |  |  |  |  |
| 27 | АС-63 | 5 | 1 | Казаренко Павел | KazarenkoPavel | [dir](./students/KazarenkoPavel) | [Catsker](https://github.com/Catsker) |  |  |  |  |  |  |
| 19 | АС-63 | 6 | 1 | Карпеш Никита | KarpeshNikita | [dir](./students/KarpeshNikita) | [Frosyka](https://github.com/Frosyka) |  |  |  |  |  |  |
| 11 | АС-63 | 7 | 1 | Козлович Антон | KozlovichAnton | [dir](./students/KozlovichAnton) | [Anton777kozlovich](https://github.com/Anton777kozlovich) |  |  |  |  |  |  |
| 15 | АС-63 | 8 | 1 | Козловская Анна | KozlovskayaAnna | [dir](./students/KozlovskayaAnna) | [annkrq](https://github.com/annkrq) |  |  |  |  |  |  |
| 21 | АС-63 | 9 | 1 | Колодич Максим | KolodichMaksim | [dir](./students/KolodichMaksim) | [proxladno](https://github.com/proxladno) |  |  |  |  |  |  |
| 29 | АС-63 | 10 | 1 | Крагель Алина | KragelAlina | [dir](./students/KragelAlina) | [Alina529](https://github.com/Alina529) |  |  |  |  |  |  |
| 44 | АС-63 | 11 | 2 | Куликович Иван | KulikovichIvan | [dir](./students/KulikovichIvan) | [teenage717](https://github.com/teenage717) |  |  |  |  |  |  |
| 34 | АС-63 | 12 | 2 | Кульбеда Кирилл | KulbedaKirill | [dir](./students/KulbedaKirill) | [fr0ogi](https://github.com/fr0ogi) |  |  |  |  |  |  |
| 13 | АС-63 | 13 | 2 | Кухарчук Илья | KukharchukIlya | [dir](./students/KukharchukIlya) | [IlyaKukharchuk](https://github.com/IlyaKukharchuk) |  |  |  |  |  |  |
| 40 | АС-63 | 14 | 1 | Логинов Глеб | LoginovGleb | [dir](./students/LoginovGleb) | [gleb7499](https://github.com/gleb7499) |  |  |  |  |  |  |
| 18 | АС-63 | 15 | 2 | Мороз Евгений | MorozEvgeniy | [dir](./students/MorozEvgeniy) | [EugeneFr0st](https://github.com/EugeneFr0st) |  |  |  |  |  |  |
| 3 | АС-63 | 16 | 2 | Никифоров Александр | NikiforovAleksandr | [dir](./students/NikiforovAleksandr) | [woQhy](https://github.com/woQhy) |  |  |  |  |  |  |
|   | АС-63 | 17 | 2 | Поплавский Владислав | PoplavskiyVladislav | [dir](./students/PoplavskiyVladislav) | [ImRaDeR1](https://github.com/ImRaDeR1) |  |  |  |  |  |  |
| 26 | АС-63 | 18 | 2 | Савко Павел | SavkoPavel | [dir](./students/SavkoPavel) | [1nsirius](https://github.com/1nsirius) |  |  |  |  |  |  |
| 25 | АС-63 | 19 | 1 | Соколова Маргарита | SokolovaMargarita | [dir](./students/SokolovaMargarita) | [Ritkas33395553](https://github.com/Ritkas33395553) |  |  |  |  |  |  |
| 38 | АС-63 | 20 | 2 | Стельмашук Иван | StelmashukIvan | [dir](./students/StelmashukIvan) | [KulibinI](https://github.com/KulibinI) |  |  |  |  |  |  |
| 39 | АС-63 | 21 | 2 | Тунчик Антон | TunchikAnton | [dir](./students/TunchikAnton) | [Stis25](https://github.com/Stis25) |  |  |  |  |  |  |
| 16 | АС-63 | 22 | 2 | Филипчук Дмитрий | FilipchukDmitriy | [dir](./students/FilipchukDmitriy) | [kuddel11](https://github.com/kuddel11) |  |  |  |  |  |  |
| 9 | АС-63 | 23 | 2 | Ярмола Александр | YarmolaAleksandr | [dir](./students/YarmolaAleksandr) | [alexsandro007](https://github.com/alexsandro007) |  |  |  |  |  |  |
| 8 | АС-63 | 24 | 2 | Ярмолович Александр | YarmolovichAleksandr | [dir](./students/YarmolovichAleksandr) | [yarmolov](https://github.com/yarmolov) |  |  |  |  |  |  |
| 37 | АС-64 | 1 | 1 | Белаш Александр | BelashAleksandr | [dir](./students/BelashAleksandr) | [went2smoke](https://github.com/went2smoke) |  |  |  |  |  |  |
| 7 | АС-64 | 2 | 1 | Брызгалов Юрий | BryzgalovYuriy | [dir](./students/BryzgalovYuriy) | [Gena-Cidarmyan](https://github.com/Gena-Cidarmyan) |  |  |  |  |  |  |
| 12 | АС-64 | 3 | 1 | Будник Анна | BudnikAnna | [dir](./students/BudnikAnna) | [annettebb](https://github.com/annettebb) |  |  |  |  |  |  |
| 33 | АС-64 | 4 | 1 | Булавский Андрей | BulavskiyAndrey | [dir](./students/BulavskiyAndrey) | [andrei1910bl](https://github.com/andrei1910bl) |  |  |  |  |  |  |
| 43 | АС-64 | 5 | 2 | Бурак Илья | BurakIlya | [dir](./students/BurakIlya) | [burakillya](https://github.com/burakillya) |  |  |  |  |  |  |
| 17 | АС-64 | 6 | 1 | Горкавчук Никита | GorkavchukNikita | [dir](./students/GorkavchukNikita) | [Exage](https://github.com/Exage) |  |  |  |  |  |  |
| 4 | АС-64 | 7 | 1 | Евкович Андрей | EvkovichAndrey | [dir](./students/EvkovichAndrey) | [Andrei21005](https://github.com/Andrei21005) |  |  |  |  |  |  |
| 14 | АС-64 | 8 | 1 | Иванюк Иван | IvanyukIvan | [dir](./students/IvanyukIvan) | [JonF1re](https://github.com/JonF1re) |  |  |  |  |  |  |
| 36 | АС-64 | 9 | 1 | Игнаткевич Кирилл | IgnatkevichKirill | [dir](./students/IgnatkevichKirill) | [pyrokekw](https://github.com/pyrokekw) |  |  |  |  |  |  |
| 22 | АС-64 | 10 | 1 | Кашпир Дмитрий | KashpirDmitriy | [dir](./students/KashpirDmitriy) | [Dima-kashpir](https://github.com/Dima-kashpir) |  |  |  |  |  |  |
| 30 | АС-64 | 11 | 1 | Котковец Кирилл | KotkovetsKirill | [dir](./students/KotkovetsKirill) | [Kirill-Kotkovets](https://github.com/Kirill-Kotkovets) |  |  |  |  |  |  |
| 6 | АС-64 | 12 | 2 | Кужир Владислав | KuzhirVladislav | [dir](./students/KuzhirVladislav) | [XD-cods](https://github.com/XD-cods) |  |  |  |  |  |  |
| 35 | АС-64 | 13 | 2 | Немирович Дмитрий | NemirovichDmitriy | [dir](./students/NemirovichDmitriy) | [goryachiy-ugolek](https://github.com/goryachiy-ugolek) |  |  |  |  |  |  |
| 2 | АС-64 | 14 | 2 | Попов Алексей | PopovAleksey | [dir](./students/PopovAleksey) | [LexusxdsD](https://github.com/LexusxdsD) |  |  |  |  |  |  |
| 31 | АС-64 | 15 | 2 | Рабченя Максим | RabchenyaMaksim | [dir](./students/RabchenyaMaksim) | [benwer9q](https://github.com/benwer9q) |  |  |  |  |  |  |
| 28 | АС-64 | 16 | 1 | Ровнейко Захар | RovneykoZakhar | [dir](./students/RovneykoZakhar) | [Zaharihnio](https://github.com/Zaharihnio) |  |  |  |  |  |  |
| 41 | АС-64 | 17 | 2 | Смердина Анастасия | SmerdinaAnastasiya | [dir](./students/SmerdinaAnastasiya) | [KotyaLapka](https://github.com/KotyaLapka) |  |  |  |  |  |  |
| 1 | АС-64 | 18 | 2 | Хомич Виталий | KhomichVitaliy | [dir](./students/KhomichVitaliy) | [VitlyaNB](https://github.com/VitlyaNB) |  |  |  |  |  |  |
| 43 | Test | 0 | 0 | Тестов Тест Тестович | TestovTestTestovich | [dir](./students/TestovTestTestovich) |  |  |  |  |  |  |  |

<!-- STUDENTS_TABLE_END -->
