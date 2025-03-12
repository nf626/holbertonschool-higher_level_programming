#!/usr/bin/python3
""" Model City Module"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """City class"""

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement="auto",
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state_id'), nullable=False)
