from redis import StrictRedis


# 拼接数据库uri
def get_db_uri(db_conf):
    uri = '{backends}+{engine}://{user}:{possword}@{host}:{port}/{db}'.format(
        backends=db_conf.get('BACKENDS'),
        engine=db_conf.get('ENGINE'),
        user=db_conf.get('USER'),
        possword=db_conf.get('POSSWORD'),
        host=db_conf.get('HOST'),
        port=db_conf.get('PORT'),
        db=db_conf.get('DATABASE')
    )
    return uri


class Config(object):
    # 公共配置
    Debug = False
    Test = False
    Online = False
    SECRET_KEY = '1234567980dsjhkfcndkvmndfklgsdg'
    SESSION_TYPE = 'redis'
    SESSION_KEY_PREFIX = 'app:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DebugConfig(Config):
    Debug = True
    # redis配置
    SESSION_REDIS = StrictRedis(host='127.0.0.1', db=6)
    # 数据库配置
    DATABASE = {
        'ENGINE': 'pymysql',
        'BACKENDS': 'mysql',
        'USER': 'zd',
        'POSSWORD': 'zhangding',
        'HOST': '101.132.145.148',
        'PORT': '3306',
        'DATABASE': 'flask02'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestConfig(Config):
    Test = True
    # redis配置
    SESSION_REDIS = StrictRedis(host='127.0.0.1', db=7)
    # 数据库配置
    DATABASE = {
        'ENGINE': 'pymysql',
        'BACKENDS': 'mysql',
        'USER': 'zd',
        'POSSWORD': 'zhangding',
        'HOST': '101.132.145.148',
        'PORT': '3306',
        'DATABASE': 'flask02_test'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class OnelineConfig(Config):
    Oneline = True
    # redis配置
    SESSION_REDIS = StrictRedis(host='127.0.0.1', db=8)
    # 数据库配置
    DATABASE = {
        'ENGINE': 'pymysql',
        'BACKENDS': 'mysql',
        'USER': 'zd',
        'POSSWORD': 'zhangding',
        'HOST': '101.132.145.148',
        'PORT': '3306',
        'DATABASE': 'flask02_online'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


conf = {
    'debug': DebugConfig,
    'test': TestConfig,
    'oneline': OnelineConfig
}
