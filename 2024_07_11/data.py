import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os

def get_areas()->list[tuple]:
    # 建立連線
    conn:psycopg2.extensions.connection = psycopg2.connect(os.environ
    ['myPOSTGRESQL'])

    data={}
    with conn: #自動 commit
        with conn.cursor() as cursor:
            sql='''
            select distinct sarea  
            from ubike_data;
            '''
            cursor.execute(sql)
            data=cursor.fetchall()

    conn.close()
    return data

