import os

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql:///postgres:@localhost/'
database_name = 'vms'


class BaseConfig:
  ''' Base Config '''
  SECRET_KEY = 'secret key'
  DEBUG = False
  BCRYPT_LOG_ROUNDS = 13
  SQLACHEMY_TRACK_MODIFICATION = False

class TestingConfig(BaseConfig):
  ''' Testing Config '''
  DEBUG = True
  TESTING = True
  BCRYPT_LOG_ROUNDS = 4
  SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + 'test'
  PRESERVE_CONTEXT_ON_EXCEPTION = False

class DevelopmentConfig(BaseConfig):
  ''' Development Config '''
  DEBUG = False
  BCRYPT_LOG_ROUNDS = 1
  SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name

class ProductionConfig(BaseConfig):
  ''' Production Config '''
  SECRET_KEY = '123'
  DEBUG = False
  SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name # @ todo add production database URI




