import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'sqlite:////Programs/SQLite/data/books.db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('fixtures/data.json', 'r') as f:
    data = json.load(f)
for publisher in data['publishers']:
    p = Publisher(id=publisher['id'], name=publisher['name'])
    session.add(p)
session.commit()

for book in data['books']:
    b = Book(id=book['id'], title=book['title'],
             id_publisher=book["id_publisher"])
    session.add(b)
session.commit()

for shop in data['shops']:
    sh = Shop(id=shop['id'], name=shop['name'])
    session.add(sh)
session.commit()

for stock in data['stocks']:
    st = Stock(id=stock['id'], id_book=stock['id_book'],
               id_shop=stock['id_shop'], count=stock['count'])
    session.add(st)
session.commit()

for sale in data['sales']:
    s = Sale(id=sale['id'], price=sale['price'],
             date_sale=sale['date_sale'], id_stock=sale['id_stock'],
             count=sale['count'])
    session.add(s)
session.commit()
session.close()
