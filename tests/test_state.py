#!/usr/bin/python3
"""
A test module to test the functionality of the State
"""

from models.state import State
import unittest
import json
import inspect
import pep8
import time

class TestStateDocs(unittest.TestCase):
    """
    Testing if docs are present and PEP valid
    """
    def test_state_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state_class_docs(self):
        self.assertTrue(len(State.__doc__) > 4)

class TestState(unittest.TestCase):
    """
        Tests the state class
    """

    def test_state_str_representation(self):
        """test that the str method has the correct output"""

        inst = State()
        string = "[State] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_state_to_dict(self):
        """
        Test conversion of object attributes to dictionary for json
        """

        my_state = State()
        my_state.first_name = "Betty"
        my_state.last_name = "Bar"
        my_state.email = "airbnb@mail.com"
        my_state.password = "root"
        d = my_state.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "first_name",
                          "last_name",
                          "email",
                          "password",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'State')
        self.assertEqual(d['first_name'], "Betty")
        self.assertEqual(d['last_name'], "Bar")
        self.assertEqual(d['email'], "airbnb@mail.com")
        self.assertEqual(d['password'], "root")

    def test_json_file_content(self):
        """
        Tests the content of the json file for state.id
        """
        my_state = State()
        my_state.first_name = "Betty"
        my_state.last_name = "Bar"
        my_state.email = "airbnb@mail.com"
        my_state.password = "root"
        my_state.save()

        with open('file.json', encoding="utf=8") as file:
            check_dic = json.load(file)
        stringy = "State." + my_state.id
        self.assertEqual(check_dic.get(stringy), my_state.to_dict())
