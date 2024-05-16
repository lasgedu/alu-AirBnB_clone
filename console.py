#!/usr/bin/python3
"""
Console Module
"""
import cmd
from models import storage
from shlex import split
from datetime import datetime
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Console Class
    """
    prompt = "(hbnb) "

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        """
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        obj = storage.all()[key]
        try:
            attr_type = type(getattr(obj, args[2]))
            setattr(obj, args[2], attr_type(args[3]))
        except AttributeError:
            setattr(obj, args[2], args[3])
        obj.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
