from sqlalchemy import create_engine, Column, String, Integer, Float, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


Base = declarative_base()


class Readings(Base):
    __tablename__ = "aquarium_sensor_readings"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    time = Column("time", DATETIME)
    temperature = Column("temperature",  Float)
    humidity = Column("humidity", Float)
    status = Column("status", String)

    def __init__(self, time, temperature, humidity, status):
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.status = status

    def __repr__(self):
        return f"{self.time}: {self.temperature}°C | {self.humidity}%  |  Status: {self.status}"

# Create file database and connect to the sqlite db and creates tables from the classes that extends base
engine = create_engine(f"sqlite:///database/mydb.db", echo=True)
Base.metadata.create_all(bind=engine)
# Create a sessionmaker and create an instance
Session = sessionmaker(bind=engine)
session = Session()
# add and commit the new record

## average of about 2 inches of water is evaporated from their fish tanksgetting as high as 5 inches in a week
# dehumidifier will increase the evaporation from the fish tank natural process in the aquarium life cycle
#increase humidity start evaporation / dehumidifier
#increase/dec temp / fan


def store_readings(temperature, humidity, status):
    readings = Readings(datetime.now(), temperature, humidity, status)
    session.add(readings)
    session.commit()


def get_all_readings():
    return session.query(Readings).all()


def get_all_warnings():
    return session.query(Readings).filter(Readings.status != 'normal')


def get_last_readings():
    return session.query(Readings).order_by(Readings.id.desc()).first()


def get_highest_readings():
    return session.query(Readings).order_by(Readings.temperature.desc()).first()
