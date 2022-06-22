import os
from dotenv import load_dotenv

class Config():
    
    MAIL_DEBUG = True
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
    MAIL_PASSWORD = 'Utecdbp12345'
    MAIL_PORT = 465
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    
    UPLOAD_FOLDER = './static/img/'

    SQLALCHEMY_DATABASE_URI = os.getenv('PSQL_PASSWORD')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv('SECRET_KEY')
