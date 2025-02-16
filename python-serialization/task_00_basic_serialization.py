#!/usr/bin/env python3
"""serialization and  deserialize module"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialise function"""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """Deserialise function"""
    with open(filename, encoding="utf-8") as file:
        file_load = json.load(file)
        return file_load
