#!/usr/bin/python3

""" Student to disk and reload """


class Student:
    """ defines a student by public instance attributes """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ If attrs is a list of strings, only attribute names
        contained in this list must be retrieved """
        if isinstance(attrs, list):
            return {key: getattr(self, key) for key in attrs
                    if isinstance(key, str) and key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for key, attr in json.items():
            if key in self.__dict__:
                setattr(self, key, attr)
        return self.__dict__
