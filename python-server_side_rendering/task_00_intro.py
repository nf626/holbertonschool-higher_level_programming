#!/usr/bin/python3
""" Creating a Simple Templating Program """
import os
from string import Template

if __name__ == '__main__':

    file_path = '/holbertonschool-higher_level_programming/python-server_side_rendering/template.txt'

    def generate_invitations(template, attendees):
        """generate invites"""
        
        path = os.path.exists(file_path)
        print(path)

        try:
            if isinstance(template, str):
                print(template)
        except:
            raise TypeError("Not string")

        try:
            if isinstance(attendees, dict):
                print(attendees)
        except:
            raise TypeError("Not dict")


        try:
            temp = Template(template)
            print(temp.safe_substitute(name="attendees"))
        except:
            raise ValueError("Cannot open")

