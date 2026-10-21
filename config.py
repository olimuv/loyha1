"""
OmniAI - Konfiguratsiya fayli
Barcha muhit sozlamalari shu yerda boshqariladi.
"""

import os
from datetime import timedelta
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()


class Config:
    """Asosiy konfiguratsiya sinfi."""
    
    # -----------------------------------------------------------------
    # Flask xavfsizlik kaliti
    # Production muhitida kamida 32 ta tasodifiy belgidan iborat bo'lsin
    # -----------------------------------------------------------------
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # -----------------------------------------------------------------
    # Ma'lumotlar bazasi
    # -----------------------------------------------------------------
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///omniAI.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # True qilsang, SQL so'rovlarni ko'rasan (debug uchun)
    
    # -----------------------------------------------------------------
    # Session sozlamalari
    # -----------------------------------------------------------------
    SESSION_COOKIE_HTTPONLY = True  # JavaScript orqali session o'qilmasin
    SESSION_COOKIE_SAMESITE = 'Lax'  # CSRF hujumlardan himoya
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # -----------------------------------------------------------------
    # CSRF himoyasi
    # -----------------------------------------------------------------
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = 3600  # 1 soat (sekundlarda)
    
    # -----------------------------------------------------------------
    # Rate limiting
    # -----------------------------------------------------------------
    RATELIMIT_DEFAULT = os.environ.get('RATELIMIT_DEFAULT', '200 per hour')
    RATELIMIT_STORAGE_URL = os.environ.get('RATELIMIT_STORAGE_URL', 'memory://')
    RATELIMIT_HEADERS_ENABLED = True
    
    # -----------------------------------------------------------------
    # AI Provider sozlamalari
    # -----------------------------------------------------------------
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
    # AI ishlatsangiz, qaysi model ishlatilishini belgilang
    AI_MODEL = os.environ.get('AI_MODEL', 'gpt-3.5-turbo')
    # Har bir so'rovdagi maksimal token soni (xarajatni nazorat qilish uchun)
    AI_MAX_TOKENS = int(os.environ.get('AI_MAX_TOKENS', '500'))
    
    # -----------------------------------------------------------------
    # Ilovaning asosiy URL
    # -----------------------------------------------------------------
    BASE_URL = os.environ.get('BASE_URL', 'http://localhost:5000')
    
    # -----------------------------------------------------------------
    # Fayl yuklash sozlamalari (kelajak uchun)
    # -----------------------------------------------------------------
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}


class DevelopmentConfig(Config):
    """Mahalliy ishlab chiqish muhiti uchun konfiguratsiya."""
    DEBUG = True
    TESTING = False
    # Development'da HTTPS talab qilinmaydi
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    """Test muhiti uchun konfiguratsiya."""
    DEBUG = True
    TESTING = True
    # Testlarda alohida SQLite ma'lumotlar bazasi
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False  # Testlarda CSRF tekshirilmaydi
    RATELIMIT_ENABLED = False  # Testlarda rate limit o'chiriladi
    SESSION_COOKIE_SECURE = False
    # Testlarda AI haqiqatan chaqirilmasin
    OPENAI_API_KEY = ''


class ProductionConfig(Config):
    """Production (ishlab chiqarish) muhiti uchun konfiguratsiya."""
    DEBUG = False
    TESTING = False
    # Production'da albatta HTTPS ishlatilsin
    SESSION_COOKIE_SECURE = True
    # Production'da PostgreSQL tavsiya etiladi
    # DATABASE_URL muhit o'zgaruvchisi orqali beriladi


# Muhit nomiga qarab kerakli konfiguratsiyani tanlash
config_map = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


def get_config():
    """FLASK_ENV ga qarab mos konfiguratsiyani qaytaradi."""
    env = os.environ.get('FLASK_ENV', 'development')
    return config_map.get(env, DevelopmentConfig)
