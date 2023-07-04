#!/usr/bin/python3
"""
Module for the file storage class
"""


import json


class FileStorage():
    """
    Class called file storage
    """
    def __init__(self, file_path, objects):
        self.__file_path = file_path
        self.__objects = objects

    @property
    def all(self):
        """
        Get the obj dict
        """
        return self.__objects

    @new.setter
    def new(self, obj):
        """
        Setting in new dict
        """
        key loop thing here
        self.__objects = value

    def save(self):
        """
        serializes json to file
        """

    def reload(self):
        """
        deserializes json to file
        """
