#!/usr/bin/python3
"""
A test module to test the functionality of the BaseModel
"""

from models.user import User
import unittest
import json
import inspect
import pep8
from datetime import datetime as dt
import time

class TestUserDocs(unittest.TestCase):
    """
    Testing if docs are present and PEP valid
    """
    def test_user_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_class_docs(self):
        self.assertTrue(len(User.__doc__) > 4)

class TestUser(unittest.TestCase):
    """
        Tests the user class
    """

    def test_user_str_representation(self):
        """test that the str method has the correct output"""

        inst = User()
        string = "[User] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_user_to_dict(self):
        """
        Test conversion of object attributes to dictionary for json
        """

        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        d = my_user.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "first_name",
                          "last_name",
                          "email",
                          "password",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'User')
        self.assertEqual(d['first_name'], "Betty")
        self.assertEqual(d['last_name'], "Bar")
        self.assertEqual(d['email'], "airbnb@mail.com")
        self.assertEqual(d['password'], "root")

    def test_json_file_content(self):
        """
        Tests the content of the json file for user.id
        """
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()

        with open('file.json', encoding="utf=8") as file:
            check_dic = json.load(file)
        stringy = "User." + my_user.id
        self.assertEqual(check_dic.get(stringy), my_user.to_dict())
