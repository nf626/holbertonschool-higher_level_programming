#!/usr/bin/env python3
"""Serializing and Deserializing XML module"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialise to xml"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        c_element = ET.SubElement(root, key)
        c_element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """deserialise from xml"""
    tree = ET.parse(filename)
    root = tree.getroot()

    tree_dict = {child.tag: child.text for child in root}

    return tree_dict
