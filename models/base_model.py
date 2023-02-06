#!/usr/bin/python3
"""
Class BaseModel that defines all common
attributes/methods for other classes.
"""

from uuid import uuid4
from datetime import datetime
import models import storage


class BaseModel():
    """
    Class BaseModel that defines all common
    attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the instances attributes
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            s = '%Y-%m-%dT%H:%M:%S.%f'
            self.created_at = datetime.strptime(self.created_at, s)
            self.updated_at = datetime.strptime(self.updated_at, s)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Prints: [<class name>] (<self.id>) <self.__dict__>
        """

        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
myDict = self.__dict__.copy()
        myDict['__class__'] = self.__class__.__name__
        myDict['created_at'] = self.created_at.isoformat()
        myDict['updated_at'] = self.updated_at.isoformat()
        return myDict
