#!/usr/bin/python3
"""
    Project 0x00. AirBnB clone - The console
        console.py
            entry point for command interpreter
"""

import cmd
import re
import shlex
import models
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand contains the entry point of the command interpreter"""
    prompt = '(hbnb) '
    classes = {
            "Amenity": Amenity,
            "BaseModel": BaseModel,
            "City": City,
            "Place": Place,
            "Review": Review,
            "State": State,
            "User": User}

    def do_quit(self, args):
        """quit command to exit the program"""
        raise SystemExit

    def do_EOF(self, args):
        """EOF command to exit the program"""
        raise SystemExit

    def emptyline(self):
        """Empty line or ENTER entered by user should not execute anything"""
        return False

    def do_create(self, args):
        """
        checks if given a class name, if not,
            prints ** class name missing **
        if so, creates new instance and prints its id,
        if class name doesn't exist,
            prints ** class name doesn't exist**
        """
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args in HBNBCommand.classes.keys():
            instance = HBNBCommand.classes[args]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Based on class name, prints string representation of an instance"""
        # creates a list of strings from args and assigns to parse_args
        parse_args = args.split()
        if len(parse_args) == 0:
            # if no argument is given,
            print("** class name missing **")
            return

        elif len(parse_args) < 2:
            # if parse_args is less than 2, input is incomplete, or
            if (parse_args[0] in HBNBCommand.classes) is True:
                # if no id is given, print
                print("** instance id missing **")
                return
            else:
                # if not given a valid class name
                print("** class doesn't exist **")
                return

        try:
            # if parse args is within dict
            if (parse_args[0] in HBNBCommand.classes) is True:
                # string format: 'class.id'
                class_id = '.'.join(parse_args)
                objs = storage.all()
                # search in JSON file with the key 'class.id'
                print(objs[class_id])
            else:
                print("** class doesn't exist **")
        except Exception:
            print("** no instance found **")

    def do_destroy(self, args):
        """Based on an class name, deletes an instance"""
        # checks if args is empty or None
        if args == "" or args is None:
            print("** class name missing **")
        else:
            # checks if args is in class_dict, or less than 2
            parsed = args.split(' ')
            if parsed[0] not in HBNBCommand.classes.keys():
                print("** class doesn't exist **")
            elif len(parsed) < 2:
                print("** instance id missing **")
            else:
                # checks key for proper format, and if its found
                key = "{}.{}".format(parsed[0], parsed[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        Structure: all [class name] or all
        """
        # prints the whole file
        args = shlex.split(args)
        obj_list = []
        if len(args) == 0:
            for value in models.storage.all().values():
                obj_list.append(str(value))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        elif args[0] in HBNBCommand.classes:
            for key in models.storage.all():
                if args[0] in key:
                    obj_list.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(obj_list), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        """
        prompt_args = args.split()

        if len(prompt_args) == 0:
            # if no argument is passed, print
            print("** class name missing **")
            return

        if (prompt_args[0] in self.classes) is True:
            # checks if the class name exists
            if len(prompt_args) < 2:
                print("** instance id missing **")
                return
        else:
            # if class name doesn't exist, print
            print("** class doesn't exist **")
            return
        # stores strings from split to key
        key = str(prompt_args[0]) + '.' + str(prompt_args[1])
        objs = storage.all()

        if (key in objs) is False:
            # if value stored in key is within dictonary
            print("** no instance found **")
            return
        elif len(prompt_args) < 3:
            # if args contains class name but no attribute, print
            print("** attribute name missing **")
            return
        elif len(prompt_args) < 4:
            # if args contains class name, id, and attribute,
            # but no value to update
            print("** value missing **")
            return
        # using eval, we cast to correct attribute type
        objs[key].__dict__[prompt_args[2]] = eval(prompt_args[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
