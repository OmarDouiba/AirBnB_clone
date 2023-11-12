#!/usr/bin/python3
"""
console.py module
"""
from cmd import Cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(Cmd):
    """
    Interactive command interpreter for HBNB project.

    Attributes:
        prompt: print (hbnb) and
        waiting for the commands
        class_name: Class Attribute list
        classes in Airbnb Project

    Methods:
        do_create(self, args): Create a new
        instance of a class.
        do_show(self, args): Show information
        about an instance.
        do_destroy(self, args): Delete an instance.
        do_all(self, args): Print all instances.
        emptyline(self): Print all instances.
        do_quit(self, args): Quit the command
        interpreter.
        do_EOF(self, args): Exit on EOF (Ctrl+D).
    """
    prompt = "(hbnb) "
    class_name = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review}
    # count = 0

    def do_create(self, args):
        """
        Create a new instance of a class.

        - create <class name>
        Example:
            create BaseModel
        """
        args_list = args.split()
        # print("--> {}".format(args_list))

        if not args_list:
            print("** class name missing **")

        elif args_list[0] in self.class_name.keys():
            new_obj = self.class_name[args_list[0]]()
            new_obj.save()
            print(new_obj.id)
            # self.count += 1
            # print(self.count)
            # print(new_obj)

        else:
            print("** class doesn't exist **")

        # if not args_list:
        #     print("** class name missing **")
        # else:
        #     for arg in args_list[:]:
        #         for key, val in self.class_name.items():
        #             if key == arg.strip():
        #                 obj = self.class_name[key]()
        #                 print(obj.id)
        #                 obj.save()
        #             elif arg not in self.class_name.keys():
        #                 print("** class doesn't exist **")

    def do_show(self, args):
        """
        Show information about an instance.

        - show <class name> <id>
        Example:
            show BaseModel 1234-1234-1234
        """
        args_list = shlex.split(args)

        if len(args_list) < 1:
            print("** class name missing **")
        elif args_list[0] not in self.class_name.keys():
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")

        else:
            id_list = []
            key_list = []

            for key in models.storage.all().keys():
                key_list = key.split('.')[1]
                id_list.append(key_list)

            if args_list[1] in id_list:
                key = ".".join([args_list[0], args_list[1]])
                # key = f"{args_list[0]}.{args_list[1]}"
                obj = models.storage._FileStorage__objects
                print(obj[key])
            else:
                return print("** no instance found **")

    def do_destroy(self, args):
        """
        Delete an instance.

        - destroy BaseModel 1234-1234-1234
        Example:
            show <class name> <id>
        """
        args_list = shlex.split(args)

        if len(args_list) < 1:
            print("** class name missing **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            input_key = f"{args_list[0]}.{args_list[1]}"
            obj = models.storage._FileStorage__objects

            if input_key in obj.keys():
                del obj[input_key]
                models.storage.save()
            else:
                return print("** no instance found **")

    def do_all(self, args):
        """
        Print all instances.

        - destroy <class name> <id>
        Example:
            destroy BaseModel 1234-1234-1234
        """
        args_list = shlex.split(args)
        obj = models.storage._FileStorage__objects

        obj_list = []
        if len(args_list) == 0:
            for val in obj.values():
                obj_list.append(str(val))
        elif args_list[0] in self.class_name.keys():
            for key, val in obj.items():
                key = key.split(".")[0]
                if args_list[0] == key:
                    obj_list.append(str(val))
        else:
            return print("** class doesn't exist **")
        print(obj_list)

    def do_update(self, arg):
        """Update command to add or update attributes"""
        """
        method that updates an instance/object based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"
        """
        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        # print("do_update: {}".format(args))
        if args[0] not in HBNBCommand.class_name.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] not in models.storage\
                                              ._FileStorage__objects.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = models.storage._FileStorage__objects[args[0]+'.'+args[1]]
            if args[2] in obj.__dict__.keys():
                try:
                    if args[3].isdigit():
                        args[3] = int(args[3])
                    elif args[3].replace('.', '', 1).isdigit():
                        args[3] = float(args[3])
                except AttributeError:
                    pass
                setattr(obj, args[2], args[3])
            else:
                try:
                    if args[3].isdigit():
                        args[3] = int(args[3])
                    elif args[3].replace('.', '', 1).isdigit():
                        args[3] = float(args[3])
                except AttributeError:
                    pass
                setattr(obj, args[2], args[3])
            HBNBCommand.class_name[args[0]].save(obj)

    def emptyline(self):
        """Do nothing on empty line."""
        # return ""
        # pass
        return False

    def do_quit(self, args):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, args):
        """Exit on EOF (Ctrl+D)."""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
