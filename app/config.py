import os

class Config:
    """Asosiy Flask sozlamalari"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///your_database.db'  # Ma'lumotlar bazasi manzili

class DevelopmentConfig(Config):
    """Dasturlash rejimi uchun sozlamalar"""
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev_database.db'

class TestingConfig(Config):
    """Sinov rejimi uchun sozlamalar"""
    TESTING = True
    DATABASE_URI = 'sqlite:///test_database.db'

class ProductionConfig(Config):
    """Ishlab chiqarish rejimi uchun sozlamalar"""
    DATABASE_URI = 'postgresql://user:password@localhost/prod_db'

class RoleConfig:
    """Foydalanuvchi rollari va URL prefikslarini sozlash"""
    USERS_ROLE = 'users'
    ADMINS_ROLE = 'admins'
    TEACHERS_ROLE = 'teachers'
    OWNERS_ROLE = 'owners'
    STARISA_ROLE = 'starisa'
    KURATR_ROLE = 'kuratr'

    USER_URL_PREFIX = '/users'
    ADMIN_URL_PREFIX = '/admins'
    TEACHER_URL_PREFIX = '/teachers'
    OWNER_URL_PREFIX = '/owners'
    STARISA_URL_PREFIX = '/starisa'
    KURATR_URL_PREFIX = '/kuratr'

    ROLE_URLS = {
        USERS_ROLE: USER_URL_PREFIX,
        ADMINS_ROLE: ADMIN_URL_PREFIX,
        TEACHERS_ROLE: TEACHER_URL_PREFIX,
        OWNERS_ROLE: OWNER_URL_PREFIX,
        STARISA_ROLE: STARISA_URL_PREFIX,
        KURATR_ROLE: KURATR_URL_PREFIX,
    }

# To�g�ri rejimni tanlash uchun Flask ilovasida ishlatish
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
