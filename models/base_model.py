#!/usr/bin/python3
"""BaseModel module"""

import uuid
from datetime import datetime
import models  # added

class BaseModel:
    """BaseModel class"""
    
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)  # line to link BaseModel to FileStorage

    def __str__(self):
        """String representation of BaseModel"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()  # line to call save method of storage

    def to_dict(self):
        """Return dictionary representation of BaseModel"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
