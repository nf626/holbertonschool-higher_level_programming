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
    x = session.query(State).first()
    print(f"{x.id}: {x.name}")

    # CLose session
    session.close()
