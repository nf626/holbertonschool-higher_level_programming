""" Creating a Simple Templating Program """
import os
from string import Template

def generate_invitations(template, attendees):
    """generate invites"""
    
    try:
        if isinstance(template, str):
            print(template)
    except:
        raise ValueError("Not string")

    try:
        if isinstance(attendees, dict):
            print(attendees)
    except:
        raise ValueError("Not dict")


    #with open(template, 'w', encoding="utf-8") as temp:

