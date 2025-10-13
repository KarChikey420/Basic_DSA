import pandas as pd
from sqlalchemy import create_engine
import psycopg2

conn = psycopg2.connect(
    user='postgres',
    password='root',
    host='localhost',
    database='mydb'
)

cur=conn.cursor()

df=pd.read_sql_query('select * from student',conn)
df.head()

create_engine='postgresql://postgres:root@localhost:5432/mydb'

df.to_sql('student',create_engine,if_exists='replace',index=False)

