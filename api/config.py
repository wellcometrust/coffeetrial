import os


class BaseConfig:
    """Base configuration"""
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'apiuebgo8ven834npgebubqa87uw4naoeuribudru3493ifiwenlijndagfl'
    SMTP_HOST = 'smtp.office365.com'
    SMTP_PORT = 587
    FROM_EMAIL = ''
    FROM_PASSWORD = ''


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = \
        "postgresql://{user}:{password}" \
        "@{host}/coffeetrial".format(
            user=os.environ['DATABASE_USER'],
            password=os.environ['DATABASE_PASSWORD'],
            host=os.environ['PGHOST']
        )


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_DATABASE_URI = \
        "postgresql://{user}:{password}" \
        "@{host}/coffeetrial?sslmode=require".format(
            user=os.environ['DATABASE_USER'],
            password=os.environ['DATABASE_PASSWORD'],
            host=os.environ['PGHOST']
        )
