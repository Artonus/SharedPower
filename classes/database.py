import os
import uuid
import shelve
import hashlib
from hashlib import blake2b, blake2s

class DB:
    
    def __init__(self, name): # Set the database file and the data holders 
        self.__dataset = shelve.open('{0}/db/{1}.db'.format(os.getcwd(), name))
        self.__data = {}
        self.__keys = []
        self.__values = []

    def load(self, name): # Load any database files into the data holder
        self.__dataset = shelve.open('{0}/db/{1}.db'.format(os.getcwd(), name))

    def save(self): # Save the database file and clear the cache
        self.__dataset.sync()
        self.__dataset.close()

    def uuid(self): # Return a UUID
        return uuid.uuid4().hex

    def hash(self, value, key="eb6ec15daf9546254f0809"): # Return a Hashed value of a value
        self.__key = hashlib.sha224(key.encode("utf-8")).hexdigest()
        self.__hash = blake2b(key=self.__key.encode("utf-8"), digest_size=32)
        self.__hash.update(value.encode("utf-8"))
        return self.__hash.hexdigest()

    def show(self): # Return all data stored in the database
        return self.__dataset

    # check if object already contains a key!
    def add(self, key, object):  # Add new entries to the database
        if key in self.listKeys(key):  # prevent overriding existing key
            raise Exception("Can't duplicate objects")
            return
        self.__dataset[key] = object 

    def remove(self, key): # Remove an entry from the database
        del self.__dataset[key]

    def keys(self): # Return a List of all keys in the database
        self.__keys = list(self.__dataset.keys())
        return self.__keys

    def count(self): # Return the number of entries in the database
        return len(self.__dataset)

    def check(self, key): # Return a check if an entry is in the database
        return key in self.__dataset

    def append(self, key, object): # Append new entries to the database
        self.__data = self.__dataset[key]
        self.__data.append(object)
        self.__dataset[key] = self.__data

    def update(self, key, object): # Update the value of an entry
        self.__dataset[key] = object 
    
    def reform(self, key, keys, object): # Update the value of an entries dictionary value
        self.__dataset[key][keys] = object

    def listAll(self, key): # Return a dictionary's of all keys pairs of an entries dictionary
        self.__data = dict(self.__dataset[key])
        return self.__data

    def listKeys(self, key):  # Return a list of all keys in an entries dictionary
        return list(self.__dataset[key])

    def listValues(self, key): # Return a list of all values in an entries dictionary
        for keys in self.listkeys(key):
            self.__values.append(self.__dataset[key][keys])
        return self.__values