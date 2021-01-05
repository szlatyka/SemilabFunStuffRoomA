from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, VARCHAR, BLOB, DateTime, Boolean
from sqlalchemy.orm import sessionmaker
Base = declarative_base()


class Group(Base):
    __tablename__ = "Groups"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, unique=True)

class User(Base):
    __tablename__ = "Users"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, unique=True)
    password = Column('password', VARCHAR)
    group_id = Column('groupid', Integer, ForeignKey(Group.id))

class Question(Base):
    __tablename__ = "Questions"

    id = Column('id', Integer, primary_key=True)
    question = Column('question', String)
    image = Column('image', BLOB)
    answer = Column('answer', String)
    hint = Column('hint', String)

class Round(Base):
    __tablename__  = "Round"

    id = Column('id', Integer, primary_key=True)
    group_id = Column('groupid', Integer, ForeignKey(Group.id))
    user_id = Column('userid', Integer, ForeignKey(User.id))
    start_time = Column('start_time', DateTime)
    end_time = Column('end_time', DateTime)
    hint_used = Column('hint_used', Boolean)
