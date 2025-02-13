#!/usr/bin/env python3
"""serialization and  deserialize module"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialise function"""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(data, file)
    print(f"{filename}")

def load_and_deserialize(filename):
    """Deserialise function"""
    with open(filename, mode="r", encoding="utf-8") as file:
        deserial = json.loads(file)
    return deserial
