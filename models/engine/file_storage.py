#!/usr/bin/python3
"""
Module for the file storage class
"""
import json


class FileStorage():
    """
    Class called file storage
    """

    """
    Class attribute file storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Get the obj dict
        """
        return self.__objects

    def new(self, obj):
        """
        COnverting object to dictionary
        """
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file
        """
        with open(self.__file_path, 'w') as serial_obj:
            json.dump(self.__objects, serial_obj)

    def reload(self):
        """
        deserializes json file to __objects attribute
        """
        try:
            with open(self.__file_path, 'r') as json_string:
                self.__objects = json.load(json_string)
        except:
            pass
