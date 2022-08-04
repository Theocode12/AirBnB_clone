#!/usr/bin/python3
"""
Base Model in which our Airbnb will be based on
"""

from datetime import datetime as dt
from models import storage
import uuid


class BaseModel(object):
    """
    Name: BaseModel
    use: An abstraction in which other classes will be based

    public attribute:
        id - unique identifier for each basemodel
        created_at - time in which object was created
        updated_at - time in which object is updated at
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the object dict with important attributes

        Attributes:
            id - id of the object
            created_at - time in which object was created
            updated_at - time in which object is updated at
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = dt.fromisoformat(value)
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """
        Return the string representation of each class
        """

        cls_name = self.__class__.__name__
        str_rep = "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
        return str_rep

    def save(self):
        """
        Updates the public instance attribute
        """

        self.updated_at = dt.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dict containing all the keys and
        values of __dict__ instance
        """

        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = type(self).__name__
        created_at = dict_rep["created_at"]
        dict_rep["created_at"] = dt.isoformat(created_at)
        updated_at = dict_rep["updated_at"]
        dict_rep["updated_at"] = dt.isoformat(updated_at)

        return dict_rep
