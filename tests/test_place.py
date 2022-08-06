#!/usr/bin/python3
"""
A test module to test the functionality of the Place
"""

from models.place import Place
import unittest
import json
import inspect
import pep8
import time

class TestPlaceDocs(unittest.TestCase):
    """
    Testing if docs are present and PEP valid
    """
    def test_place_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_place_class_docs(self):
        self.assertTrue(len(Place.__doc__) > 4)

class TestPlace(unittest.TestCase):
    """
        Tests the place class
    """

    def test_place_str_representation(self):
        """test that the str method has the correct output"""

        inst = Place()
        string = "[Place] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_place_to_dict(self):
        """
        Test conversion of object attributes to dictionary for json
        """

        my_place = Place()
        my_place.first_name = "Betty"
        my_place.last_name = "Bar"
        my_place.email = "airbnb@mail.com"
        my_place.password = "root"
        d = my_place.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "first_name",
                          "last_name",
                          "email",
                          "password",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'Place')
        self.assertEqual(d['first_name'], "Betty")
        self.assertEqual(d['last_name'], "Bar")
        self.assertEqual(d['email'], "airbnb@mail.com")
        self.assertEqual(d['password'], "root")

    def test_json_file_content(self):
        """
        Tests the content of the json file for place.id
        """
        my_place = Place()
        my_place.first_name = "Betty"
        my_place.last_name = "Bar"
        my_place.email = "airbnb@mail.com"
        my_place.password = "root"
        my_place.save()

        with open('file.json', encoding="utf=8") as file:
            check_dic = json.load(file)
        stringy = "Place." + my_place.id
        self.assertEqual(check_dic.get(stringy), my_place.to_dict())
