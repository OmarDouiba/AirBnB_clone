#!/usr/bin/python3
"""
Unittest for the FileStorage class
"""
import unittest
import pep8
import json
# import sys
from os import path, remove
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """define variables and methods"""
    pass