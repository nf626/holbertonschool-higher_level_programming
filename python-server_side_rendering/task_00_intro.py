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
    
    try:
        if isinstance(attendees, dict):
            print(attendees)
    except:
        raise ValueError("Not dict")

    if not template:
        return {'error': 'template is empty'}
    
    if not attendees:
        return {'error': 'attendees is empty'}

    for i, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")

        invite = template.replace("{name}", name)
        invite = invite.replace("{event_title}", event_title)
        invite = invite.replace("{event_date}", str(event_date))
        invite = invite.replace("{event_location}", event_location)

        with open(f"output_{i}.txt", "w", encoding="utf-8") as f:
            f.write(invite)
        print(invite)
