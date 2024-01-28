#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

# Import classes based on the value of HBNB_TYPE_STORAGE
if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload storage after it's instantiated
storage.reload()
