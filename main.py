import pyodbc
import config
import redis
import json


def redisConnect():
    r = redis.Redis(host=config.redis_server, port=6379, password=config.redis_password, username=config.redis_user)
    return r


if __name__ == '__main__':
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+config.server+';DATABASE='+config.database+';UID='+config.username+';PWD='+ config.password)
    cursor = cnxn.cursor()
    cursor.execute('SELECT TOP 5 [code], [Остаток] as Count, [Цена] as Price FROM sales.w_остаток_как_на_сайте')
    row = cursor.fetchone()
    rc = redisConnect()
    uts = {}

    while row:
        uts.update({str(row[0]): {"Count": float(row[1]), "Price": float(row[2])}})
        row = cursor.fetchone()

    print(uts)
    with rc.pipeline() as pipe:
        for ut_id, properties in uts.items():
            rc.set(ut_id, json.dumps(properties))

    pipe.execute()
    rc.get(ut_id)



