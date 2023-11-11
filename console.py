#!/usr/bin/python3
"""
console.py module
"""
from cmd import Cmd
import shlex
import models
from models.base_model import BaseModel


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
        "BaseModel": BaseModel}
    # count = 0

    def do_create(self, args):
        """Create a new instance of a class."""
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
        """Show information about an instance."""
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
        """Delete an instance."""
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
        """Print all instances."""
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

    def do_update(self, args):
        pass

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
