""" Creating a Simple Templating Program """


def generate_invitations(template, attendees):
    """generate invites"""
    
    try:
        if isinstance(template, str):
            return
    except:
        raise ValueError("Not string")

    try:
        if isinstance(attendees, list) or all(isinstance(attendee, dict) for attendee in attendees):
            return
    except:
        raise ValueError("Not list of dict")


    if not template:
        return {'error': 'template is empty'}
    
    if not attendees:
        return {'error': 'attendees is empty'}

    for i, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A")
        event_title = attendee.get("event_title", "N/A")
        event_date = attendee.get("event_date", "N/A")
        event_location = attendee.get("event_location", "N/A")
        
        if event_date is None:
            event_date = "N/A"
        else:
            event_date = event_date

        if event_location is None:
            event_location = "N/A"
        else:
            event_location = event_location

        try:
            invite = template.replace("{name}", name)
            invite = invite.replace("{event_title}", event_title)
            invite = invite.replace("{event_date}", str(event_date))
            invite = invite.replace("{event_location}", event_location)
        except:
            raise AttributeError("Error")

        with open(f"output_{i}.txt", "w", encoding="utf-8") as f:
            f.write(invite)
        print(invite)
