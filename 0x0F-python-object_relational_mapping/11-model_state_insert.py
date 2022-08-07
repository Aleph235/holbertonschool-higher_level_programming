#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine, Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    Louisiana = State(name='Louisiana')
    session.add(Louisiana)
    session.commit()
    print(Louisiana.id)
    session.close()
