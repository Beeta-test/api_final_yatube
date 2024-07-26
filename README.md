# api_final
api_final\napi final\n

## Описание

Проект **api_final** — это RESTful API для социальной сети, в которой пользователи могут создавать, просматривать и управлять постами и комментариями. Он предоставляет функциональность для взаимодействия с ресурсами социальной сети через API, обеспечивая возможность работы с пользователями, постами и комментариями.

## Установка

Чтобы развернуть проект на локальной машине, выполните следующие шаги:

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/Beeta-test/api_final_yatube
    ```

2. Перейдите в директорию проекта:
    ```bash
    cd api_final
    ```

3. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```

4. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

5. Примените миграции:
    ```bash
    python manage.py migrate
    ```

6. Запустите сервер:
    ```bash
    python manage.py runserver
    ```

Теперь проект доступен по адресу http://127.0.0.1:8000/.

## Примеры запросов к API

### Получение публикаций

**Запрос:**
```http
GET /api/v1/posts/

**Ответ:**
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]
}

### Добавление комментария

**Запрос:**
```http
POST /api/v1/posts/{post_id}/comments/

**Ответ:**
{
    "text": "string"
}

### Обновление публикации

**Запрос:**
```http
PUT /api/v1/posts/{id}/

**Ответ:**
{
    "text": "string",
    "image": "string",
    "group": 0
}

### Частичное обновление публикации

**Запрос:**
```http
PATCH /api/v1/posts/{id}/

**Ответ:**
{
    "text": "string",
    "image": "string",
    "group": 0
}

### Удаление комментария

**Запрос:**
```http
Delete /api/v1/posts/{post_id}/comments/{id}/

**Ответ:**
...

### Получить JWT-токен

**Запрос:**
```http
POST /api/v1/jwt/create/

**Ответ:**
{
    "username": "string",
    "password": "string"
}

### Получить JWT-токен

**Запрос:**
```http
POST /api/v1/jwt/create/

**Ответ:**
{
    "username": "string",
    "password": "string"
}
