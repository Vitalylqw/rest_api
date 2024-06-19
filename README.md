# REST API for SQL Backup Cleanup

## Описание

Это REST API приложение, разработанное с использованием Flask, которое принимает данные о SQL бэкапах, форматирует их и отправляет в виде сообщения через Telegram-бота. Приложение также логирует все запросы и ответы в файл.

## Функциональность

- **Начальная страница**: Простое приветственное сообщение.
- **Маршрут `/cleanup_sql_backup`**: Принимает POST-запрос с данными в формате JSON, форматирует их и отправляет пользователю через Telegram-бота.

## Требования

- Python 3.6 или выше
- Flask
- python-dotenv
- python-telegram-bot
- waitress

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/Vitalylqw/rest_api.git
    cd rest_api
    ```

2. Создайте и активируйте виртуальное окружение:

    - **На Windows:**

      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

    - **На Unix или MacOS:**

      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` в корне проекта и добавьте туда ваши переменные окружения:

    ```plaintext
    TELEGRAM_TOKEN=your-telegram-bot-token
    TELEGRAM_CHAT_ID=your-telegram-chat-id
    ```

## Использование

1. Запустите приложение:

    ```bash
    python app.py
    ```

2. Приложение будет доступно по адресу:

    ```plaintext
    * Running on http://0.0.0.0:3355/
    ```

3. Отправьте POST-запрос на маршрут `/cleanup_sql_backup` с данными в формате JSON. Пример запроса:

    ```bash
    curl -X POST http://127.0.0.1:3355/cleanup_sql_backup -H "Content-Type: application/json" -d '{
        "result": true,
        "deleted_files_count": 0,
        "remaining_files": [
            {
                "name": "bsc_backup_2024_06_19_003734_4031615.bak",
                "modification_time": "2024-06-19",
                "size": 3133275648,
                "root_directory": "E:\\sql_backup\\bsc"
            },
            {
                "name": "bsc_backup_2024_06_19_120001_9241317.bak",
                "modification_time": "2024-06-19",
                "size": 15859200,
                "root_directory": "E:\\sql_backup\\bsc"
            }
        ]
    }'
    ```

## Структура проекта

- `rest_api.py`: Основной файл приложения.
- `requirements.txt`: Файл с необходимыми зависимостями.
- `.env`: Файл с переменными окружения (не включен в репозиторий).
- `app.log`: Файл логов приложения.