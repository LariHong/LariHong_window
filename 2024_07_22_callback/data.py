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

def get_snaOfArea(area:str)->list[tuple]:
    # 建立連線
    conn:psycopg2.extensions.connection = psycopg2.connect(os.environ
    ['myPOSTGRESQL'])

    data={}
    with conn: #自動 commit
        with conn.cursor() as cursor:
            sql='''
            select sna as 站點, total as 總數,rent_bikes as 可借, retuen_bikes as 可還,mday as 時間, act as 營運狀態
            from ubike_data
            where(updatetime,sna) in(
                SELECT MAX(updatetime),sna
                FROM ubike_data
                where sarea =(%s)
                GROUP BY sna
            )
            '''
            cursor.execute(sql,(area,))
            data=cursor.fetchall()

    conn.close()
    return data
