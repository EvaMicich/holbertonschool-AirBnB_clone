#!/usr/bin/python3
"""
Module that creates the class Basemodel and all
common attributes/methods for other classes
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel instance.
        """
        attributes_list = ["id", "name", "my_number"]
        attributes_ignore_list = ["__class__"]
        attributes_datetime_list = ["created_at", "updated_at"]
        if kwargs != {}:
            for key, value in kwargs.items():
                if key in attributes_ignore_list:
                    continue
                elif key in attributes_datetime_list:
                    setattr(self, key, datetime.now().fromisoformat(value))
                elif key in attributes_list:
                    setattr(self, key, value)
                else:
                    raise ValueError(f"Unknown attribute {key}
                                       in class BaseModel")

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Return a string representation of the instance.
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Update the updated_at attribute with the current datetime.
        '''
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
