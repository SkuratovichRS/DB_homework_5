# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables

DSN = 'postgresql://postgres:postgres@localhost:5432/books'
engine = sqlalchemy.create_engine(DSN, client_encoding='utf-8')

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()
