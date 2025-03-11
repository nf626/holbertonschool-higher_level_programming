#!/usr/bin/python3
"""prints the first State object
from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Declare connection arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    # starting point
    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db}"
        )

    # generates new Session objects when called
    Session = sessionmaker(bind=engine)

    # produce new session
    session = Session()

    # print first state
    states = session.query(State).order_by(State.id).first()
    if bool(states):
        print(f"{states.id}: {states.name}")
    else:
        print("Nothing")

    # CLose session
    session.close()
