import pymysql


def outer(cls):
    instance = None

    def inner(*args, **kwargs):
        nonlocal instance
        if instance == None:
            instance = cls(*args, **kwargs)
        return instance

    return inner


@outer
class SqlTool(object):
    __instance = None

    def __init__(self, user, pwd, host, port, db):
        self.client = pymysql.connect(
            user=user,
            password=pwd,
            host=host,
            port=port,
            database=db
        )
        self.cursor = self.client.cursor()

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def query(self, sql):
        self.cursor.execute(sql)
        return self.fetch_all_to_dict(self.cursor)

    def fetch_all_to_dict(self, cursor):
        desc = [i[0] for i in cursor.description]
        result = [dict(zip(desc, col)) for col in cursor.fetchall()]
        return result
