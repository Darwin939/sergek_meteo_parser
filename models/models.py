from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, SmallInteger

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from datetime import datetime

engine = create_engine('sqlite:///sqlite3.db')

Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'sensors'
    id = Column(Integer(), primary_key=True)
    sensor_id_num = Column(Integer())
    sensor_id_string = Column(String(100), nullable=True)
    name = Column(String(100), nullable=True)
    longtitude = Column(String(100), nullable=False)
    latitude = Column(String(100), nullable=False)
    sensor_height = Column(String(100), nullable=True)
    datas = relationship("Data")

class Data(Base):
    __tablename__ = 'datas'
    id = Column(Integer, primary_key=True)
    field1 =  Column(Numeric(10, 10), nullable=True)
    field2 =  Column(Numeric(10, 10), nullable=True)
    field3 =  Column(Numeric(10, 10), nullable=True)
    field4 =  Column(Numeric(10, 10), nullable=True)
    field5 =  Column(Numeric(10, 10), nullable=True)
    created_on_their_data = Column(String(100), nullable=True)

    date_created = Column(DateTime(), default=datetime.now)
    sensor_id = Column(Integer, ForeignKey('sensors.id'))



Base.metadata.create_all(engine)