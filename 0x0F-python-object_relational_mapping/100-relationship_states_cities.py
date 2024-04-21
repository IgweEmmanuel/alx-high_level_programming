#!/usr/bin/python3
"""
Here, the code will print all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import BaseClass, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    The code will have get from the database 
    the cities.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    BaseClass.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    sessions = Session()
    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(sfr_city)

    sessions.add(state)
    sessions.commit()
    sessions.close()
