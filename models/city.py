#!/usr/bin/python3
"""
Module that contains classs city that inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class
    """
    state_id = ""
    name = ""
