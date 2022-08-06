#!/usr/bin/python3
"""
A test module to test the functionality of the City
"""

from models.city import City
import unittest
import json
import inspect
import pep8
import time

class TestCityDocs(unittest.TestCase):
    """
    Testing if docs are present and PEP valid
    """
    def test_city_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_class_docs(self):
        self.assertTrue(len(City.__doc__) > 4)

class TestCity(unittest.TestCase):
    """
        Tests the city class
    """

    def test_city_str_representation(self):
        """test that the str method has the correct output"""

        inst = City()
        string = "[City] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_city_to_dict(self):
        """
        Test conversion of object attributes to dictionary for json
        """

        my_city = City()
        my_city.first_name = "Betty"
        my_city.last_name = "Bar"
        my_city.email = "airbnb@mail.com"
        my_city.password = "root"
        d = my_city.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "first_name",
                          "last_name",
                          "email",
                          "password",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'City')
        self.assertEqual(d['first_name'], "Betty")
        self.assertEqual(d['last_name'], "Bar")
        self.assertEqual(d['email'], "airbnb@mail.com")
        self.assertEqual(d['password'], "root")

    def test_json_file_content(self):
        """
        Tests the content of the json file for city.id
        """
        my_city = City()
        my_city.first_name = "Betty"
        my_city.last_name = "Bar"
        my_city.email = "airbnb@mail.com"
        my_city.password = "root"
        my_city.save()

        with open('file.json', encoding="utf=8") as file:
            check_dic = json.load(file)
        stringy = "City." + my_city.id
        self.assertEqual(check_dic.get(stringy), my_city.to_dict())
