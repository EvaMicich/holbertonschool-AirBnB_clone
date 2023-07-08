#!/usr/bin/python3
"""
Module for the file storage class
"""
import json



class FileStorage():
    """
    Class called file storage

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
        COnverting object to dictionary of id:obj
        """
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file
        """
        new_dict = {}
        for key in self.__objects:
            new_dict[key] = self.__objects[key].to_dict()
        try:
            with open(self.__file_path, 'w') as serial_obj:
                json.dump(new_dict, serial_obj)
        except:
            pass

    def reload(self):
        """
        deserializes json file to __objects attribute
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        
        dict_classes = {
            "BaseModel": BaseModel,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }
        dict_objects  = {}
        try:
            with open(self.__file_path, 'r') as json_string:
                dict_objects = json.load(json_string)
        except:
            dict_objects  = {}
            pass
        for key, dict_object in dict_objects.items():
            current_obj_class = dict_object["__class__"]
            if current_obj_class in dict_classes:
                self.__objects[key] = dict_classes[current_obj_class](**dict_object)
            else:
                raise TypeError(f'unknown class: {current_obj_class}')
