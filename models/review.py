#!/usr/bin/python3
"""
    Review data Module
"""
from models.base_model import BaseModel
from models.user import User
from models.place import Place

class Review(BaseModel):
    """
        Review class
    """
    place_id = ""
    user_id = ""
    text = ""
