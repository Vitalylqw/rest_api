import logging
import asyncio
import os
from flask import Flask, request, jsonify
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

# Конфигурация Telegram Bot
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = Bot(token=TELEGRAM_TOKEN)

@app.route('/')
def index():
    """
    Начальная страница.
    Возвращает простое приветственное сообщение.
    """
    logging.info("Received request at / (index page)")
    return """
    <h1>Welcome to the REST API</h1>
    <p>Use the endpoint <code>/cleanup_sql_backup</code> to post your SQL backup data.</p>
    """

@app.route('/cleanup_sql_backup', methods=['POST'])
def cleanup_sql_backup():
    """
    Маршрут для обработки POST-запросов на /cleanup_sql_backup.
    Принимает данные в формате JSON, форматирует их и отправляет пользователю через Telegram-бота.
    """
    # Логирование входящего запроса
    logging.info("Received request at /cleanup_sql_backup")
    
    try:
        # Получение данных из запроса
        data = request.json
        logging.info(f"Received data: {data}")
        
        # Форматирование данных
        message = format_message(data)
        
        # Отправка сообщения через Telegram Bot
        asyncio.run(send_telegram_message(message))
        
        logging.info("Message sent to Telegram successfully")
        
        return jsonify({"status": "success"}), 200
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

def format_message(data):
    """
    Функция для форматирования данных в читаемый текстовый вид.
    """
    message = "SQL Backup Cleanup Report\n\n"
    message += f"Result: {data['result']}\n"
    message += f"Deleted Files Count: {data['deleted_files_count']}\n"
    message += "Remaining Files:\n"
    
    for file in data['remaining_files']:
        file_info = f"  - Name: {file['name']}\n"
        file_info += f"    Modification Time: {file['modification_time']}\n"
        file_info += f"    Size: {file['size']}\n"
        file_info += f"    Root Directory: {file['root_directory']}\n"
        message += file_info

    return message

async def send_telegram_message(message):
    """
    Асинхронная функция для отправки сообщения через Telegram Bot.
    """
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=3355)
    from waitress import serve
    serve(app, host='0.0.0.0', port=3355)