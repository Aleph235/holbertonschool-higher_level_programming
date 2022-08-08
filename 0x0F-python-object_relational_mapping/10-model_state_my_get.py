#!/usr/bin/python3
""" prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    mystate = session.query(State.id).filter(State.name == sys.argv[4]).first()
    if(mystate):
        print("{}".format(mystate.id))
    else:
        print('Not found')
    session.close()
