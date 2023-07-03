#!/usr/bin/python3
'''
Module that creates the class Basemodel and all
common attributes/methods for other classes
'''


import uuid
import datetime


class BaseModel:
    '''
    Base class for other classes
    '''
    def __init__(self):
        '''
        Initialize the BaseModel instance.
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

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
