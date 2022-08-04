#!/usr/bin/python3
"""
An Interpreter for my Airbnb clone
"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage
import shlex
import re
import sys


class HBNBCommand(cmd.Cmd):
    """
    A class that inherits from the cmd module
    """

    prompt = "(hbnb) "
    all_models = [
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    ]

    def precmd(self, line: str) -> str:
        """
            Runs after every input in console

            Args:
                line: the inputted text
        """
        regex = "^(\w+)\.(\w+)\(([^\)]*)"

        if re.search(regex, line):
            reg_pat = re.findall(regex, line)
            c_name, method = reg_pat[0][0], reg_pat[0][1]
            args = reg_pat[0][2]

            if args:
                temp = [arg.strip("'") for arg in reg_pat[0][2].split(", ")]
                args = " ".join(temp)
            # print(args.split(" ")[1])

            return "{} {} {}".format(method, c_name, args)
        else:
            return super().precmd(line)

    def do_EOF(self, args):
        """
        Handles the EOF command
        """

        print()
        return True

    def do_quit(self, args):
        """
        Handles the quit command
        """

        return True

    def help_quit(self):
        """
        help for the quit command
        """

        print("Quit command to exit the program")

    def do_create(self, args):
        """
        Create new instances
        """

        if args:
            parsed = shlex.split(args)
            try:
                new_obj = eval(parsed[0])()
                print(new_obj.id)
                new_obj.save()
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def help_create(self):
        msg = ["create a new instance of an object",
                "Usage: create <class name>"]
        print("\n".join(msg))

    def do_show(self, args):
        """
        Shows the string rep. of an instance based on the class name and id
        """

        args = shlex.split(args)

        if len(args) == 0:
            print("** class name missing **")

        elif len(args) == 1:
            if args[0] in self.all_models:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

        else:
            all_objs = storage.all()
            key = ".".join(args[:2])
            if key in all_objs:
                obj = all_objs[key]
                print(obj)
            else:
                print("** no instance found **")

    def help_show(self):
        """
        help for the "show" command
        """

        msg = ["Prints the string rep. of an ins based on class name & id",
                "Usage: show <class name> <id>"]
        print("\n".join(msg))

    def do_destroy(self, args):
        """
        Deletes an instance based onthe class name
        """

        args = shlex.split(args)

        if len(args) == 0:
            print("** class name missing **")

        elif len(args) == 1:
            if args[0] in self.all_models:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

        else:
            all_objs = storage.all()
            key = ".".join(args[:2])
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def help_destroy(self):
        """
        help for the "destroy" command
        """

        msg = ["Deletes an instance based on the class name",
                "Usage: destroy <class name> <id>"]
        print("\n".join(msg))

    def do_all(self, args):
        """
        string representation of all instances on the class(optional) provided
        """

        all_objs = storage.all()
        all_objs_list = list()
        if args:
            args = shlex.split(args)
            if args[0] in self.all_models:
                for key in all_objs:
                    if type(all_objs[key]).__name__ == args[0]:
                        all_objs_list.append(str(all_objs[key]))
            else:
                print("** class doesn't exist **")
                return
        else:
            for key in all_objs:
                all_objs_list.append(str(all_objs[key]))
        print(all_objs_list)

    def help_all(self):
        """
        help function for "all" command
        """

        msg = ["string rep. of all ins on the class(optional) provided",
                "Usage: all [<class name>]"]
        print("\n".join(msg))

    def emptyline(self):
        pass

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        """

        args = shlex.split(args)

        if len(args) == 0:
            print("** class name missing **")
            return

        if len(args) >= 1:
            if args[0] not in self.all_models:
                print("** class doesn't exist **")
                return
            if len(args) == 1:
                print("** instance id missing **")
                return

        if len(args) >= 2:
            all_objs = storage.all()
            key = ".".join(args[0:2])
            if key in all_objs:
                obj = all_objs[key]
            else:
                print("** no instance found **")
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return

        if len(args) == 3:
            print("** value missing **")
            return

        if "{" and "}" in " ".join(args[2:]):
            new_li = [sign for sign in args[2:]]
            print("".join(new_li))
        else:
            print("here")
            setattr(obj, args[2], args[3])
            obj.save()

    def help_update(self):
        """
        Help for "update" command
        """

        msg = ["updates obect with new attributes",
                "Usage: update <class name> <id> <attribute <value>"]
        print("\n".join(msg))

    def do_count(self, args):
        """
        retrieves the number of instances of a class
        """
        args = shlex.split(args)
        count = 0

        for c_names in list(storage.all().keys()):
            if c_names.split(".")[0] == args[0]:
                count += 1
        print(count)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
