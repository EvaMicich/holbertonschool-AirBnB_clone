#!/usr/bin/python3
'''
Module that creates the class Basemodel and all
common attributes/methods for other classes
'''

import uuid
from datetime import datetime


class BaseModel:
    '''
    Base class for other classes
    '''

    def __init__(self, name=None, my_number=None, id=None,
                 created_at=None, updated_at=None):
        '''
        Initialize the BaseModel instance.
        '''
        self.name = name
        self.my_number = my_number
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''
        Return a string representation of the instance.
        '''
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        '''
        Update the updated_at attribute with the current datetime.
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = f"{self.__class__.__name__}"
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
