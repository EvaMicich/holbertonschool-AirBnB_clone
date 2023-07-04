#!/usr/bin/python3
"""
Module that creates the class Basemodel and all
common attributes/methods for other classes
"""

import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage

storage = FileStorage

class BaseModel:
    """
    Base class for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel instance.
        """
        if kwargs != {}:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'name':
                    self.name = value
                elif key == 'my_number':
                    self.my_number = value
                elif key == 'created_at':
                    self.created_at = datetime.now().fromisoformat(value)
                elif key == 'updated_at':
                    self.updated_at = datetime.now().fromisoformat(value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
#            storage.new(self)

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
#        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
