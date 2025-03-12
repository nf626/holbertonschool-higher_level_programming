#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City


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

    # print all city name
    # for city in session.query(City).order_by(City.id).filter(City.state_id == State.id).all():
    #     print(f"{State.name}: ({city.id}) {city.name}")

    for city in session.query(City).join(State).join(City).filter(City.state_id == State.id).all():
        print(f"{State.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
