from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://avargas:Thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

class Item(Base):
    __tablename__ = 'items'

    id =  Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bid = relationship('Bid', backref='items')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    items = relationship('Item', backref='users')
    buy = relationship('Bid', backref='users')

class Bid(Base):
    __tablename__ = 'bids'

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

Base.metadata.create_all(engine)

andrew = User()
andrew.username = 'Andrew'
andrew.password = 'Thinkful'

dante = User()
dante.username = 'Dante'
dante.password = 'Thinkful'

andrew.baseball = Item()
andrew.baseball.name = 'Baseball'
andrew.baseball.description = 'Something that you throw'

session.add_all([andrew, dante])

print('The Auction is about to start')

print('Item up for auction is {} - {}'.format(andrew.baseball.name, andrew.baseball.description))

andrew.bid= Bid()
andrew.bid.price = input('{}, Please Enter a Whole number that you would like to bid? '.format(andrew.username))
'''
dante_bid = Bid()
dante_bid.price = input('{}, Please Enter a Whole number that you would like to bid? '.format(dante.username))
'''
session.add_all([andrew.bid, andrew.baseball])
session.commit()






