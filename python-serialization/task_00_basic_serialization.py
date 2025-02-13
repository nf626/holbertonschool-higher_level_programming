#!/usr/bin/env python3
"""serialization and  deserialize module"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, mode="w", encoding="utf-8") as file:
        return json.dump(data, file)

def load_and_deserialize(filename):
    with open(filename,encoding="utf-8") as file:
        deserial = json.loads(file)
        return deserial
