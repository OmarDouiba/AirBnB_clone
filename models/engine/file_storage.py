#!/usr/bin/python3
"""
FileStorage.py module
"""
from os import path
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
    __file_path = 'file.json'
    __objects = {}
    className = {'BaseModel': BaseModel,
                 'User': User,
                 'State': State,
                 'City': City,
                 'Amenity': Amenity,
                 'Place': Place,
                 'Review': Review}

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
            json.dump(new_dict, save_file)

    def reload(self):
        """
        function that deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                f_contents = f.read()
                dict_obj_dicts = json.loads(f_contents)
            for key in dict_obj_dicts.keys():
                obj_dict = dict_obj_dicts[key]
                # FileStorage.__objects[key] = BaseModel(**obj_dict)
                FileStorage.__objects[key] = FileStorage\
                           .className[key.split('.')[0]](**obj_dict)
        except FileNotFoundError:
            pass
