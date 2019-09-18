from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship 

engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session =  Session()

class Customer(Base):
    
    __tablename__ = 'customer'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    team = relationship('Iteam', cascade="all,delete", backref="customer")

class Iteam(Base):

    __tablename__ = 'iteam'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    time = Column(Date)
    pasta = Column(Integer)
    noodles = Column(Integer)
    pizza = Column(Integer)
    burger = Column(Integer)
    sandwich = Column(Integer)
    kitkat = Column(Integer)
    biscuits = Column(Integer)
    chocolates = Column(Integer)
    total = Column(Integer)



Base.metadata.create_all(engine)