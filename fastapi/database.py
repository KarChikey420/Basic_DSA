from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL="postgresql://postgres:"+os.getenv("database_password")+"@db.xibtivnigehtcututvkb.supabase.co:5432/postgres"
engine=create_engine(DATABASE_URL,pool_pre_ping=True)

sessionmaker=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()


print("DataBase Connected Successfully")
