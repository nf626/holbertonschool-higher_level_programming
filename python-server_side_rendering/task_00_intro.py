""" Creating a Simple Templating Program """
import os


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

    with open('output_1.txt', 'r', encoding='utf-8') as file:
        attendee_list = file.read()
