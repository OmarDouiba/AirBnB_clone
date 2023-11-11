#!/usr/bin/python3
"""
FileStorage.py module
"""
from os.path import exists
from json import dump, load
from models.base_model import BaseModel


class FileStorage():
    """
    Handles serialization and
    deserialization to a JSON file.

    Attibutes:
        __file_path: private class attribute
        contain file name
        __objects: private class attribute to store
        all objects by <class name>.id
        class_name: Class Attribute list
        classes in Airbnb Project.

    Methods:
        all(self): Return the dictionary __objects
        new(self, obj): Set in __objects
        the obj with key <obj class name>.id
        save(self): Serialize __objects
        to the JSON file (path: __file_path)
        reload(self): Deserialize the JSON
        file (path: __file_path) to __objects
    """
    __file_path = "file.json"
    __objects = {}
    class_name = {
        'BaseModel': BaseModel}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with
        key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__,
                             obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the
        JSON file (path: __file_path)"""
        new_dict = {}

        for key, obj in self.__objects.items():
            new_dict[key] = obj.to_dict()

        with open(self.__file_path, "w",
                  encoding="utf-8") as save_file:
            dump(new_dict, save_file)

    def reload(self):
        """Deserialize the JSON file
        (path: __file_path) to __objects"""
        if exists(self.__file_path):
            with open(self.__file_path,
                      "r") as read_file:
                file_data = load(read_file)

            for key, val in file_data.items():
                dict_class = val["__class__"]
                # dict_class, _ = key.split(".")
                class_n = self.class_name[dict_class]
                if dict_class == class_n.__name__:
                    self.__objects[key] = class_n(**val)
