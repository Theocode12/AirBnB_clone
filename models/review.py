#!/usr/bin/python3
"""
A module for Reveiw
"""

from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """
    A class for Review
    """

    place_id = ""
    user_id = ""
    text = ""
    