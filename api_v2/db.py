from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from snowflake.sqlalchemy import URL
import json
import os
from pathlib import Path
DIR_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = DIR_PATH.parent

# from sqlalchemy import create_engine
# ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"

# async_engine = create_async_engine(ASYNC_DB_URL, echo=True)



with open( ROOT_PATH / 'snowflack_config.json') as f: 
    config = json.load(f)

async_engine = create_engine(URL(
    account = config['account'],
    user = config['user'],
    password = config['password'],
    database = 'TEST_PREFERENCE',
    schema = 'public',
    warehouse = 'COMPUTE_WH',
    role=config['role'],
    numpy=True
))

async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine,
)

Base = declarative_base()


def get_db():
    with async_session() as session:
        yield session