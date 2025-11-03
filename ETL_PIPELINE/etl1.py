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

