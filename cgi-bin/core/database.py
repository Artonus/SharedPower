import hashlib
import json
import os
import shelve
import sqlite3
import uuid
from hashlib import blake2b, blake2s
from sqlite3 import Error
from datetime import datetime
from datetime import timedelta



class DB:
    @staticmethod
    def create_connection():    
        db_file = '{0}\db\{1}.db'.format(os.getcwd(), "sharedpower")
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)    
        return None

    @staticmethod
    def setCurrUser(user): # pass whole user 
        fileread = open(os.getcwd() + "/cgi-bin/core/appsettings.json", 'r')
        tmp = fileread.read()
        jsn = json.loads(tmp)
        fileread.close()
        filewrite = open(os.getcwd() + "/cgi-bin/core/appsettings.json", 'w')
        jsn["currUser"] = user[1]
        filewrite.write(json.dumps(jsn))
        filewrite.close()
        pass 
    @staticmethod
    def getCurrUser():
        file = open(os.getcwd() + "/cgi-bin/core/appsettings.json", 'r')
        tmp = file.read()
        jsn = json.loads(tmp)
        file.close()
        return jsn["currUser"]

    @staticmethod
    def hash(value, key="eb6ec15daf9546254f0809"): # Return a Hashed value of a value
        _key = hashlib.sha224(key.encode("utf-8")).hexdigest()
        _hash = blake2b(key=_key.encode("utf-8"), digest_size=32)
        _hash.update(value.encode("utf-8"))
        return str(_hash.hexdigest())   
    @staticmethod
    def commitAndCloseConnection(conn):
        conn.commit()
        conn.close()
        pass
    @staticmethod
    def getCurrUserData():
        conn= DB.create_connection()
        c = conn.cursor()
        c.execute("select * from users where username=?", (DB.getCurrUser(),))
        data = c.fetchall()[0]
        conn.close()
        return data
    @staticmethod
    def addBookedTool(form):        
            conn = DB.create_connection()
            c = conn.cursor()
            user = DB.getCurrUserData()
            c.execute("insert into invoices(userid, toolid, toolname, price, dateofrent) values (?, ?, ?, ?, ?)", (user[0], form["toolid"].value, form["inputName"].value, int(form["inputPrice"].value) * int(float(form["inputSelect"].value)), form["inputDate"].value))
            enddate = datetime.strptime(form["inputDate"].value, '%Y-%m-%d') + timedelta(days=int(float(form["inputSelect"].value))) 
            strdate = enddate.strftime('%Y-%m-%d')
            c.execute("insert into booked_tools(userid, toolid, startdate, enddate) values(?, ?, ?, ?)", (user[0], form["toolid"].value, form["inputDate"].value, strdate))
            DB.commitAndCloseConnection(conn)
    
    def __init__(self, name): # Set the database file and the data holders 
        self.__dataset = shelve.open('{0}/cgi-bin/db/{1}.db'.format(os.getcwd(), name))
        self.__data = {}
        self.__keys = []
        self.__values = []

    def load(self, name): # Load any database files into the data holder
        self.__dataset = shelve.open('{0}/cgi-bin/db/{1}.db'.format(os.getcwd(), name))

    def save(self): # Save the database file and clear the cache
        self.__dataset.sync()
        self.__dataset.close()

    def uuid(self): # Return a UUID
        return uuid.uuid4().hex    

    def show(self): # Return all data stored in the database
        return self.__dataset

    # check if object already contains a key!
    def add(self, key, object):  # Add new entries to the database
        if self.listKeys(key) != None:  # prevent overriding existing key
            return False
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

    def listKeys(self, key): # Return a list of all keys in an entries dictionary
        try:
            if key in self.__dataset:
                return dict(self.__dataset[key])
        except Exception as ex:        
            print("No such key in dataset", ex)

    def listValues(self, key): # Return a list of all values in an entries dictionary
        for keys in self.listKeys(key):
            self.__values.append(self.__dataset[key][keys])
        return self.__values
