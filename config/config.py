"""
Конфигурация проекта Currency ETL
"""
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Настройки API
API_BASE_URL = "https://api.frankfurter.app"
BASE_CURRENCY = os.getenv("BASE_CURRENCY", "USD")
TARGET_CURRENCIES = ["EUR", "GBP", "JPY", "CAD", "CHF", "CNY", "RUB"]

# Пути к данным
RAW_DATA_PATH = "data/raw"
PROCESSED_DATA_PATH = "data/processed"

# Настройки логирования
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")