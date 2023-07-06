#!/usr/bin/python3
"""
Module for the file storage class
"""
import json


"""
class BaseModelEncoder(json.JSONEncoder):

    A json encoding tool to turn BaseModel ojects into dictionary,
    as intermediate for a json.dump conversion
    def default(self, obj):
        if isinstance(obj, BaseModel):
            return obj.to_dict()
        return super().default(obj)
"""

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
