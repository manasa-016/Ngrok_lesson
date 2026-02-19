from db import Base
from sqlalchemy import Column,Integer,String,DateTime,Text
from datetime import datetime

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,index=True)
    password=Column(String)
    api_key=Column(String)
    name=Column(String)

class Address(Base):
    __tablename__="addresses"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,index=True)
    address=Column(String)
    city=Column(String)
    state=Column(String)
    zip_code=Column(String)
    country=Column(String)
    
class Order(Base):
    __tablename__="orders"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,index=True)
    address_id=Column(Integer,index=True)
    order_date=Column(DateTime,default=datetime.now())
    total_amount=Column(Integer,index=True)
    status=Column(String)
    