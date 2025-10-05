import psycopg2
import pandas as pd
from sqlalchemy import create_engine

source=psycopg2.connect(
    host="localhost",
    database="mydb",
    user="postgres",
    password="root"  
)

dest=create_engine('postgresql://postgres:root@localhost:5432/mydb1')
print("database")

cur=source.cursor()

query="select * from student"

df=pd.read_sql_query(query,source)

df.to_sql("student",dest,if_exists='replace',index=False)

