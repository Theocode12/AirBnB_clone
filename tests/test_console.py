#!/usr/bin/python3
"""
    Tests for console
"""

from io import StringIO
import sys
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.review import Review
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class TestForConsole(unittest.TestCase):
    """
        class of console test
    """

    def test_create_base_model(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], BaseModel)

    def test_create_user(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], User)

    def test_create_state(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], State)

    def test_create_review(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], Review)

    def test_create_place(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], Place)

    def test_create_amenity(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], Amenity)

    def test_create_city(self):
        """
            tests the create command
        """
        FileStorage._FileStorage__objects = dict()  # string mangling
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            all_objs = storage.all()
            for key in all_objs.keys():
                self.assertIsInstance(all_objs[key], City)

    def test_for_missing_class_name(self):
        """
            tests for missing class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_for_wrong_class_name(self):
        """
            tests for the wrong class name
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create mymodel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_show_base_model(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "BaseModel.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_show_user(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "User.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_show_state(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "State.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_show_review(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "Review.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_show_place(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "Place.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_show_city(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "City.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_show_amenity(self):
        """
            tests the show command on valid class names
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            my_baseid = f.getvalue().strip('\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity {}".format(my_baseid))
            all_objs = storage.all()
            k_string = "Amenity.{}".format(my_baseid)
            self.assertEqual(f.getvalue().strip('\n'),
                             str(all_objs.get(k_string)))

    def test_for_missing_class_name_show(self):
        """
            tests for missing class name using the show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_for_wrong_class_name_show(self):
        """
            tests for the wrong class name using show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show mymodel")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_for_wrong_class_name_show(self):
        """
            tests for the wrong class name using show command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show ")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
