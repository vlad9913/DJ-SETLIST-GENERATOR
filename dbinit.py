# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:46:39 2021

@author: Vlad
"""

#from database.database_config import Config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker


"""
DATABASE = 'postgresql'
USER = 'postgres'
PASSWORD = 'soyamilk'
HOST = 'localhost'
PORT = '5432'
DB_NAME = 'postgres'
"""


db = create_engine('postgresql://postgres:soyamilk@localhost:5432/postgres',pool_size=10,max_overflow=-1)
#NEW_DB_NAME = 'my_database'


#conn = engine.connect()
#conn.execute("commit")


#conn.execute("create database "+ NEW_DB_NAME)
#conn.close()


Session = sessionmaker(db)  
session = Session()

#conn = db.connect()
#conn.execute('ALTER TABLE "Setlists" ALTER COLUMN date TYPE INTEGER USING date::numeric')


base = declarative_base()
#base.metadata.create_all(db)

