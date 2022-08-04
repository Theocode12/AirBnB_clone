#!/usr/bin/python3
"""
File storage engine
"""

import json
import re


class FileStorage(object):
    """
    A module to Organise or file storage engine
    """

    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """
        Returns all the object created
        """

        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the __object attributes
        """

        self.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """
        Saves object to json file
        """

        nw_dict = dict()
        for key, val in self.__objects.items():
            nw_dict[key] = val.to_dict()

        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(nw_dict, file)

    def reload(self):
        """
        Deserializes objects from files
        """

        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.city import City
        from models.review import Review
        from models.state import State

        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                old_dict = json.load(file)

        except Exception:
            pass

        else:
            for key, val in old_dict.items():
                cls_name = re.findall("^\w+", key)
                self.__objects[key] = eval(cls_name[0])(**val)
