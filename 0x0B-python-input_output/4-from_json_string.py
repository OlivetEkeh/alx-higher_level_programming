#!/usr/bin/python3

"""a function that returns an object"""


def from_json_string(my_str):
    """returns an object (data structure) represented by a JSON string:"""
    import json
    return json.loads(my_str)
