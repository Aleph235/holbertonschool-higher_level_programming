#!/usr/bin/python3
"""lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
"""
import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    path = ('mysql+mysqldb://{}:{}@localhost/{}'
              .format(sys.argv[1], sys.argv[2],
                      sys.argv[3]))

    engine = create_engine(path, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State)\
                        .filter(State.name.contains('a%')):
                        if state is None:
                            print("Nothing")
                        else:
                            print("{}: {}".format(state.id, state.name))
