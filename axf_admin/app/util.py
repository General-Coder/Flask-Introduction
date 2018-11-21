from math import ceil

import uuid
from sqlalchemy import create_engine
import hashlib
from datetime import datetime, timedelta

engine = create_engine(
    'mysql+pymysql://zd:zhangding@101.132.145.148:3306/axf_project'
)


def enc_pwd(pwd):
    sha256 = hashlib.sha256()
    sha256.update(pwd.encode('utf-8'))
    return sha256.hexdigest()


def create_unique_str():
    uuid_str = str(uuid.uuid4()).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()


def data_to_dict(cursor):
    heads = [i[0] for i in cursor.description]
    return [dict(zip(heads, col)) for col in cursor.fetchall()]


def get_no_sale():
    con = engine.connect()
    # 获取15天之前的数据
    fifteen_days = datetime.now() - timedelta(days=15)

    sql = """
        SELECT 
         DISTINCT i.goods_id 
        FROM
         axf_order AS o
        LEFT JOIN 
          axf_orderitem AS i
        ON 
        o.id = i.order_id
        WHERE 
        o.create_time >'{my_time}'
        AND 
        o.create_time < now();
    """.format(my_time=str(fifteen_days))

    res = con.execute(sql)
    goods_ids = data_to_dict(res.cursor)
    # 有一个集合
    good_tmp = []
    for i in goods_ids:
        good_tmp.append(list(i.values())[0])
    all_good_sql = '''
        select id,storenums,price from axf_goods;    
    '''
    all_goods = data_to_dict(con.execute(all_good_sql).cursor)
    all_good_tmp = []
    # for i in all_goods:
    #     all_good_tmp.append(i.values())
    # #转成集合相减
    # result = list(set(all_good_tmp) - set(good_tmp))
    # print(result)

    goods_maps = {}
    for i in all_goods:
        goods_maps[i.get('id')] = {
            'storenums': i.get('storenums'),
            'price': i.get('price')
        }
    # 转成集合相减
    result = list(set(goods_maps.keys()) - set(good_tmp))
    return result


def get_data():
    get_goods_day = 3
    my_time = datetime.now() - timedelta(days=get_goods_day * 2)
    sql = """
        SELECT
        i.goods_id,SUM(i.num) as sum_num,ag.storenums
        FROM
         axf_order as o 
        LEFT JOIN 
          axf_orderitem as i
        ON 
          o.id = i.order_id
          LEFT JOIN 
          axf_goods as ag 
          ON 
          i.goods_id = ag.id
          WHERE 
          o.create_time > '{my_time}'
          AND 
          o.create_time < now()
          GROUP BY 
          i.goods_id
    
    """.format(my_time=my_time)
    con = engine.connect()
    res = con.execute(sql)
    result = data_to_dict(res.cursor)
    bh_map = {}
    #求平均值，然后乘以get_goods_data就得到了未来三天需要的商品数量
    for i in result:
        i['need'] = ceil(float(i.get('sum_num') / (get_goods_day * 2) * get_goods_day))
        if i['need'] >= i['storenums']:
            bh_map[i.get('goods_id')] = {
                'need':i['needs'],
                'storenums':i['storenums']
            }
    print(result)

