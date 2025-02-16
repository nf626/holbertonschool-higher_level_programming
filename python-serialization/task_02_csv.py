#!/usr/bin/env python3
"""csv to json module"""
import csv
import json


def convert_csv_to_json(csvFile):
    """convert csv to json"""
    try:
        with open(csvFile, mode="r", encoding="utf-8") as csvf:
            csvReader = list(csv.DictReader(csvf))
        with open("data.json", mode="w", encoding="utf-8") as csv_file:
            json.dump(csvReader, csv_file)
        return True
    except (FileNotFoundError):
        return False
