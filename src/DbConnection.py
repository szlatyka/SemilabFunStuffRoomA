from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, VARCHAR, BLOB, DateTime, Boolean
from sqlalchemy.orm import sessionmaker

import Entities


def getDbSession():

    engine = create_engine('sqlite:///sqlapi.db', echo=True)
    Entities.Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    return session

#user = User()
#user.id = 0
#user.name = "Bob"
#session.add(user)
#session.commit()
#session.close()
