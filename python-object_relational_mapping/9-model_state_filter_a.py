#!/usr/bin/python3
"""lists all State objects that contain
the letter a from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


if __name__ == '__main__':
    # Declare connection arguments
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    # starting point
    engine = create_engine(
        f"mysql+mysqldb://{user}: {password}@localhost:3306/{db}"
    )

    # generates new Session objects when called
    Session = sessionmaker(bind=engine)

    # produce new session
    session = Session()

    # print states with 'a'
    for state in session.query(State).filter(State.name.contains('a')):
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
