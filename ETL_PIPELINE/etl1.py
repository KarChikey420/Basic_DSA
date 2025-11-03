import pandas as pd
from sqlalchemy import create_engine
import psycopg2

def get_db_connection():
   try:
        conn=psycopg2.connect(
            user='postgres',
            password='root',
            host='localhost',
            database='mydb'
        )
   except psycopg2.Error as e:
       print("Error connecting to database:",e)
   return conn

def fetch_student_data(conn):
    try:
        query="select * from student"
        df=pd.read_sql_query(query,conn)   
    except psycopg2.Error as e:
        print("Error fetching data:",e)
    return df

def transform_data(df):
    df_cleaned=df.dropna()
    return df_cleaned
