#!/usr/bin/python3
"""
A test module to test the functionality of the BaseModel
"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import unittest
import json
import inspect
import pep8
from datetime import datetime as dt
import time
import os

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class TestFileStorageDocs(unittest.TestCase):
    """
    Testing if docs are present and if the files are PEP valid
    """

    def test_base_pep8_conformance(self):
        """
        Testing for pep8 conformance"
        """

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_docs(self):
        """
        Testings for class docs
        """

        self.assertTrue(len(FileStorage.__doc__) > 4)

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def test_all_returns_dict(self):
        """Test that all returns the FileStorage.__objects attr"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""

        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_save(self):
        """Test that save properly saves objects to file.json"""

        os.remove("file.json")
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = type(instance).__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))


    def test_reload(self):
        """Tests if reload return the object from the file"""

        os.remove("file.json")
        storage = FileStorage()
        nw_dict = {}
        for key, value in classes.items():
            obj = value()
            nw_dict[type(obj).__name__ + "." + obj.id] = obj
        FileStorage._FileStorage__objects = nw_dict
        storage.save()
        storage.reload()
        self.assertEqual(nw_dict, FileStorage._FileStorage__objects)
