#!/usr/bin/env python3
"""csv to json module"""
import csv, json


def convert_csv_to_json(csvFile):
    """convert csv to json"""
    j_file = 'data.json'
    with open(csvFile, encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)
        js_file = json.dump(csvReader, j_file)
