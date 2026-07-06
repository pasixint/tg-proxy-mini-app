import os
from dotenv import load_dotenv

# Явно указываем абсолютный путь к файлу .env на твоем компе
dotenv_path = r"C:\projects\tg-proxy-mini-app\.env"

# Принудительно загружаем
load_dotenv(dotenv_path=dotenv_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEB_APP_URL = os.getenv("WEB_APP_URL")

# Проверим, прочиталось ли теперь
if not BOT_TOKEN:
    print("❌ ПРЯМОЙ ПУТЬ НЕ СРАБОТАЛ. Текущая папка скрипта:", os.getcwd())