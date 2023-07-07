#!/usr/bin/python3
"""
Module that contains the class named Review that inherits BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class
    """
    place_id = ""
    user_id = ""
    text = ""
