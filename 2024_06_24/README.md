>## postgres 連線python
```
import psycopg2

# 建立連線
conn = psycopg2.connect("postgresql://tvdi_ljd4_user:FSspEufknGYVE8Ve7s4saMNY54XuOAG8@dpg-cpscsh08fa8c739535bg-a.singapore-postgres.render.com/tvdi_ljd4")

# sql操作
cursor=conn.cursor()
sql=''' 
create table if not exists student(
	student_id serial primary key,
	name varchar(20) not null,
	major varchar(20)
);
'''
cursor.execute(sql)
conn.commit()   #如果不用 with ...  as ... 要加這行
cursor.close()

#關閉連線
conn.close()
```