#!/usr/bin/python3
"""
A user class to model users
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    The User Class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
