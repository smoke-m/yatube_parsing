from sqlalchemy import Column, Date, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, declared_attr


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


class MondayPost(Base):

    author = Column(String)
    date = Column(Date)
    text = Column(Text)

    def __repr__(self):
        return self.author


def creating_engine():
    engine = create_engine('sqlite:///sqlite.db')
    Base.metadata.create_all(engine)
    return Session(engine)
