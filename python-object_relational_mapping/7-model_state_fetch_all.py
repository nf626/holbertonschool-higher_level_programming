#!/usr/bin/python3
"""lists all State objects
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
    "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
    user, password, db)
    )

    # generates new Session objects when called
    Session = sessionmaker(bind=engine)

    # produce new session
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
