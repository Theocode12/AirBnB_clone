#!/usr/bin/python3
"""
A test module to test the functionality of the BaseModel
"""

from models.base_model import BaseModel
import unittest
import json
import inspect
import pep8
from datetime import datetime as dt
import time

class TestBaseModelDocs(unittest.TestCase):
    """
    Testing if docs are present and if the files are PEP valid
    """

    def test_base_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_class_docs(self):
        self.assertTrue(len(BaseModel.__doc__) > 4)

class TestBaseModel(unittest.TestCase):
    """
    Tests the BaseModel class
    """

    def test_str_representation(self):
        """test that the str method has the correct output"""

        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_uuid(self):
        """Test uuid given to instances"""

        my_model1 = BaseModel(self)
        my_model2 = BaseModel(self)
        self.assertNotEqual(my_model1, my_model2)
        self.assertIs(type(my_model1.id), str)
        self.assertIs(type(my_model2.id), str)

    def test_created_at(self):
        """Tests created at"""
        my_model1 = BaseModel(self)
        self.assertIs(type(my_model1.created_at), dt)

    def test_updated_at(self):
        "Tests updated at"""
        my_model1 = BaseModel(self)
        self.assertIs(type(my_model1.updated_at), dt)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""

        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.isoformat())
        self.assertEqual(new_d["updated_at"], bm.updated_at.isoformat())

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""

        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_datetime_attributes(self):
        """Test that two BaseModel instances have different datetime objects
        and that upon creation have identical updated_at and created_at
        value."""

        my_model1 = BaseModel(self)
        print(my_model1.created_at)
        time.sleep(1)
        my_model2 = BaseModel(self)
        print(my_model2.created_at)
        self.assertNotEqual(my_model1.created_at, my_model2.created_at)
        self.assertNotEqual(my_model1.updated_at, my_model2.updated_at)

class TestBaseModelDict(unittest.TestCase):
    """
        Test class for Base Model Dict
    """

    def test_created_updated_type(self):
        """
            Checks for the types of created at and updated at
            before an after passed as a kwarg
        """

        mod1 = BaseModel()
        mod_dic = mod1.to_dict()

        self.assertIs(type(mod_dic.get('created_at')), str)
        self.assertIs(type(mod_dic.get('updated_at')), str)

        new_mod = BaseModel(**mod_dic)

        self.assertIs(type(new_mod.created_at), dt)
        self.assertIs(type(new_mod.updated_at), dt)

    def test_for_attr_class(self):
        """
            Checks if the attribute 'class' is present in the newly
            created instance
        """

        mod1 = BaseModel()  
        mod_dic = mod1.to_dict()
        new_mod = BaseModel(**mod_dic)

        self.assertFalse(new_mod.__dict__.get('__class__'))
