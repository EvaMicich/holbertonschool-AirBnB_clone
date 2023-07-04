#!/usr/bin/python3
"""
Module for the file storage class
"""


import json


class FileStorage():
    """
    Class called file storage

    Arguments:
    file_path: string - path to the JSON file (ex: file.json
    objects: dictionary - empty but will store all objects by <class name>.id
    """

    def __init__(self, file_path="", objects={}):
        """initial file storage"""
        self.__file_path = file_path
        self.__objects = objects

    def all(self):
        """
        Get the obj dict
        """
        return self.__objects

    def new(self, obj):
        """
        Setting in new dict
        """
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        with open(self.__file_path, 'w') as serial_obj:
            json.dump(self.__objects, serial_obj)

    def reload(self):
        """
        deserializes json to file
        """
        try:
            with open(self.__file_path, encoding="utf-8") as obj_from_json:
                return(json.load(obj_from_json))
        except:
            pass
