from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
engine = create_engine('postgresql://postgres:&Shivang5@127.0.0.1:6432/PizzaDelivery',echo=True)

Base = declarative_base()

Session = sessionmaker()


