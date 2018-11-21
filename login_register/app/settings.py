class DebugConfig(object):
    DEBUG = True
    SECRET_KEY = '1234567980dsjhkfcndkvmndfklgsdg'
    SESSION_TYPE = 'redis'
    SESSION_KEY_PREFIX = 'app:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://zd:zhangding@101.132.145.148:3306/login'