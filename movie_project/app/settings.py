import os
from redis import StrictRedis

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


CACHE = {
    'default':{
    'CACHE_TYPE':'redis',
    'CACHE_REDIS_URL':'redis://127.0.0.1:6379/9'
    },
    'debug':{
    'CACHE_TYPE':'redis',
    'CACHE_REDIS_URL':'redis://127.0.0.1:6379/10'
    }
}


def get_db_uri(db_conf):
    uri = '{backends}+{engine}://{user}:{possword}@{host}:{port}/{db}'.format(
    engine = db_conf.get('ENGINE') or 'pymysql',
    backends = db_conf.get('BACKENDS') or 'mysql',
    user = db_conf.get('USER') or 'zd',
    possword = db_conf.get('POSSWORD') or 'zhangding',
    host = db_conf.get('HOST') or '101.132.145.148',
    port = db_conf.get('PORT') or '3306',
    db = db_conf.get('DATABASE') or 'flask04'
    )

    return uri



class Config(object):
    DEBUG = False
    Test = False
    Online = False
    SECRET_KEY = '1234567980dsjhkfcndkvmndfklgsdg'
    SESSION_TYPE = 'redis'
    SESSION_KEY_PREFIX = 'app:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False

class DebugConfig(Config):
    DEBUG = True
    SESSION_REDIS = StrictRedis(host='127.0.0.1', db=6)
    DATABASE = {
        'ENGINE': 'pymysql',
        'BACKENDS': 'mysql',
        'USER': os.environ.get('DB_USER'),
        'POSSWORD': os.environ.get('DB_PWD'),
        'HOST': '101.132.145.148',
        'PORT': '3306',
        'DATABASE': 'movie'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

class TestConfig(Config):
    Test = True
    SESSION_REDIS = StrictRedis(host='127.0.0.1', db=7)
    DATABASE = {
        'ENGINE': 'pymysql',
        'BACKENDS': 'mysql',
        'USER': 'zd',
        'POSSWORD': 'zhangding',
        'HOST': '101.132.145.148',
        'PORT': '3306',
        'DATABASE': 'flask04_test'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class OnelineConfig(Config):
    Oneline = True
    SESSION_REDIS = StrictRedis(host='127.0.0.1', db=8)
    DATABASE = {
        'ENGINE': 'pymysql',
        'BACKENDS': 'mysql',
        'USER': 'zd',
        'POSSWORD': 'zhangding',
        'HOST': '101.132.145.148',
        'PORT': '3306',
        'DATABASE': 'flask04_online'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


conf = {
    'debug': DebugConfig,
    'test': TestConfig,
    'oneline': OnelineConfig
}