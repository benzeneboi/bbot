import os
from dotenv import load_dotenv

load_dotenv()

class Config:
   SQLALCHEMY_TRACK_MODIFICATIONS = False

   @staticmethod
   def init_app(app):
       pass

class DevelopmentConfig(Config):
   DEBUG=True
   SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL2')
   # Docker: 'postgresql://bb_test:password@db:5432/betbotapp'
   # local: os.getenv('DATABASE_URL')
class TestingConfig(Config):
   DEBUG = True
   TESTING = True
   SQLALCHEMY_DATABASE_URI = os.environ.get(
       "TEST_DATABASE_URL")


config = {
   'development': DevelopmentConfig,
   'testing': TestingConfig,

   'default': DevelopmentConfig}
