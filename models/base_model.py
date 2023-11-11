#!/usr/bin/python3
"""
BaseModel.py module
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    class BaseModel that defines all common
    attributes/methods for other classes

    Methods:
        __init__(self, *args, **kwargs): The constructor
        of a BaseModel
        __str__(self): Return string representation of
        the instance
        save(self): Update the updated_at attribute
        and save the instance
        to_dict(self): Return a dictionary
        representation of the instance
    """

    def __init__(self, *args, **kwargs):
        """initialize variables and methods"""
        if kwargs is not None and len(kwargs) > 0:
            # if kwargs: # cmd line equivalent to the one above
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                try:
                    if value.isdigit():
                        value = int(value)
                    elif value.replace('.', '', 1).isdigit():
                        value = float(value)
                except AttributeError:
                    pass
                setattr(self, key, value)
                # print(self.__dict__)
        # elif len(kwargs) == 0:
        #     continue
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
    # we can do type(self).__name__

    def save(self):
        """Update the updated_at attribute and
        save the instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation
        of the instance"""
        to_dict = self.__dict__.copy()
        new_dict = {}
        new_dict["__class__"] = type(self).__name__

        for k, v in to_dict.items():
            if k == "created_at" or k == "updated_at":
                new_dict[k] = datetime.isoformat(v)
            else:
                new_dict[k] = v
        return new_dict
