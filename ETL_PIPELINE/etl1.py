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

def load_data_to_db(df):
    try:
        create_engine='postgresql://postgres:root@localhost:5432/mydb'
        df.to_sql("cleaned_student",create_engine,if_exists='replace',index=False)
    except Exception as e:
        print("Error loading data to database:",e)
    print("Data loaded successfully into cleaned_student table.")

if __name__=="__main__":
    conn=get_db_connection()
    df=fetch_student_data(conn)
    df_cleaned=transform_data(df)
    load_data_to_db(df_cleaned)