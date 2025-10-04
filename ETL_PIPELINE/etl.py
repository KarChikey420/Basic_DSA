import psycopg2
import pandas as pd

conn=psycopg2.connect(
    host="localhost",
    database="mydb",
    user="postgres",
    password="root"  
)
print("database")

cur=conn.cursor()

query="select * from student"
df=pd.read_sql_query(query,conn)
print(df)
cur.close()
conn.close()

