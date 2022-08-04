#!/usr/bin/python3
"""
    File storage module
"""
import json as js
import re


class FileStorage:
    """
        File Storage Class
    """

    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """
            returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
            sets in __objects the obj with key <obj class name>.id
            Args:
                obj: object to be saved
        """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        new_dict = dict()
        for key, val in self.__objects.items():
            new_dict[key] = val.to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as filename:
            js.dump(new_dict, filename)


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
                old_dict = js.load(file)

        except Exception:
            pass

        else:
            for key, val in old_dict.items():
                cls_name = re.findall("^\w+", key)
                self.__objects[key] = eval(cls_name[0])(**val)
