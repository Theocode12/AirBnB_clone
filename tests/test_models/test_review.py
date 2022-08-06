#!/usr/bin/python3
"""
A test module to test the functionality of the Review
"""

from models.review import Review
import unittest
import json
import inspect
import pep8
import time

class TestReviewDocs(unittest.TestCase):
    """
    Testing if docs are present and PEP valid
    """
    def test_review_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_class_docs(self):
        self.assertTrue(len(Review.__doc__) > 4)

class TestReview(unittest.TestCase):
    """
        Tests the review class
    """

    def test_review_str_representation(self):
        """test that the str method has the correct output"""

        inst = Review()
        string = "[Review] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_review_to_dict(self):
        """
        Test conversion of object attributes to dictionary for json
        """

        my_review = Review()
        my_review.first_name = "Betty"
        my_review.last_name = "Bar"
        my_review.email = "airbnb@mail.com"
        my_review.password = "root"
        d = my_review.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "first_name",
                          "last_name",
                          "email",
                          "password",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'Review')
        self.assertEqual(d['first_name'], "Betty")
        self.assertEqual(d['last_name'], "Bar")
        self.assertEqual(d['email'], "airbnb@mail.com")
        self.assertEqual(d['password'], "root")

    def test_json_file_content(self):
        """
        Tests the content of the json file for review.id
        """
        my_review = Review()
        my_review.first_name = "Betty"
        my_review.last_name = "Bar"
        my_review.email = "airbnb@mail.com"
        my_review.password = "root"
        my_review.save()

        with open('file.json', encoding="utf=8") as file:
            check_dic = json.load(file)
        stringy = "Review." + my_review.id
        self.assertEqual(check_dic.get(stringy), my_review.to_dict())
