#!/usr/bin/python3
"""
    Base Model Module
"""
import uuid as uid
from datetime import datetime
from models import storage


class BaseModel:
    """
        Base Model Class
    """

    def __init__(self, *args, **kwargs) -> None:
        """
            Constructor Function
            Args:
                args: list of arguments
                kwargs: dictionary of name and value
        """
        convertt = ['created_at', 'updated_at']
        if not kwargs:
            self.id = str(uid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == '__class__':
                    pass
                elif key in convertt:  # convert to datetime object
                    self.__dict__[key] = datetime.fromisoformat(val)
                else:
                    self.__dict__[key] = val

    def __str__(self) -> str:
        """
            String Representation of Object
        """
        class_name = self.__class__.__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
            saves object to database
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Returns a dictionary containing all the keys/values of the instance
        """
        new_dic = dict()
        convertt = ['created_at', 'updated_at']

        for key, value in self.__dict__.items():
            if key in convertt:
                new_dic[key] = value.isoformat()
            else:
                new_dic[key] = value

        new_dic['__class__'] = self.__class__.__name__
        return new_dic
