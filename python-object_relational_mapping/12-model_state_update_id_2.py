#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""
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

    # add state id
    new_state = State(
        name="Louisiana"
    )
    session.add(new_state)
    session.commit()

    if new_state:
        print(f"{new_state.id}")
    else:
        print("Not found")

    # CLose session
    session.close()
