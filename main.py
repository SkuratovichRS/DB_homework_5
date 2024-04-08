import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Shop, Stock, Sale

DSN = 'sqlite:////Programs/SQLite/data/books.db'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

inp = input('Введите имя издателя без пробела')


def get_data_by_publisher(p_name: str) -> list:
    data = []
    query = (session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
             .join(Publisher).join(Stock).join(Shop).
             join(Sale).filter(Publisher.name == p_name))
    for result in query.all():
        data.append(result)
    return data


def print_data(data: list) -> None:
    result = ""
    for d in data:
        b_name, sh_name, price, date = d
        result += f'{b_name} | {sh_name} | {price} | {date} \n'
    print(result)


print_data(get_data_by_publisher(inp))
