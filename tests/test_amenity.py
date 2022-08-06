#!/usr/bin/python3
"""
A test module to test the functionality of the Amenity
"""

from models.amenity import Amenity
import unittest
import json
import inspect
import pep8
import time

class TestAmenityDocs(unittest.TestCase):
    """
    Testing if docs are present and PEP valid
    """
    def test_amenity_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_class_docs(self):
        self.assertTrue(len(Amenity.__doc__) > 4)

class TestAmenity(unittest.TestCase):
    """
        Tests the amenity class
    """

    def test_amenity_str_representation(self):
        """test that the str method has the correct output"""

        inst = Amenity()
        string = "[Amenity] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_amenity_to_dict(self):
        """
        Test conversion of object attributes to dictionary for json
        """

        my_amenity = Amenity()
        my_amenity.first_name = "Betty"
        my_amenity.last_name = "Bar"
        my_amenity.email = "airbnb@mail.com"
        my_amenity.password = "root"
        d = my_amenity.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "first_name",
                          "last_name",
                          "email",
                          "password",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'Amenity')
        self.assertEqual(d['first_name'], "Betty")
        self.assertEqual(d['last_name'], "Bar")
        self.assertEqual(d['email'], "airbnb@mail.com")
        self.assertEqual(d['password'], "root")

    def test_json_file_content(self):
        """
        Tests the content of the json file for amenity.id
        """
        my_amenity = Amenity()
        my_amenity.first_name = "Betty"
        my_amenity.last_name = "Bar"
        my_amenity.email = "airbnb@mail.com"
        my_amenity.password = "root"
        my_amenity.save()

        with open('file.json', encoding="utf=8") as file:
            check_dic = json.load(file)
        stringy = "Amenity." + my_amenity.id
        self.assertEqual(check_dic.get(stringy), my_amenity.to_dict())
