#
# This class contains functions to run database connection and data flow
#
import hashlib
import json
import os
import shelve
import shutil
import sqlite3
import uuid
from datetime import datetime, timedelta
from hashlib import blake2b, blake2s
from sqlite3 import Error


class DB:
    # establishing connection with database
    @staticmethod
    def createConnection():    
        db_file = '{0}\db\{1}.db'.format(os.getcwd(), "sharedpower")
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)    
        return None

    # setting current user to a file
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
    # getting current user from a file
    @staticmethod
    def getCurrUser():
        file = open(os.getcwd() + "/cgi-bin/core/appsettings.json", 'r')
        tmp = file.read()
        jsn = json.loads(tmp)
        file.close()
        return jsn["currUser"]

    # function to hash passwords
    @staticmethod
    def hash(value, key="eb6ec15daf9546254f0809"): # Return a Hashed value of a value
        _key = hashlib.sha224(key.encode("utf-8")).hexdigest()
        _hash = blake2b(key=_key.encode("utf-8"), digest_size=32)
        _hash.update(value.encode("utf-8"))
        return str(_hash.hexdigest())
    
    # commiting changes to database and closing connection
    @staticmethod
    def commitAndCloseConnection(conn):
        conn.commit()
        conn.close()
        pass
    
    # geting data of currently logged user
    @staticmethod
    def getCurrUserData():
        conn= DB.createConnection()
        c = conn.cursor()
        c.execute("select * from users where username=?", (DB.getCurrUser(),))
        data = c.fetchall()[0]
        conn.close()
        return data
    
    # adding values to database after user booked a tool
    @staticmethod
    def addBookedTool(form):        
        conn = DB.createConnection()
        c = conn.cursor()
        user = DB.getCurrUserData()
        
        DB.addInvoiceRecord(form)        

        if form.getvalue("inputDispatch", '').lower() in ['true', 'yes','t', '1', 'on', 'checked']:
            DB.addInvoiceRecord(form, True)

        enddate = datetime.strptime(form["inputDate"].value, '%Y-%m-%d') + timedelta(days=int(float(form["inputSelect"].value))) 
        strdate = enddate.strftime('%Y-%m-%d')
        c.execute("insert into booked_tools(userid, toolid, startdate, enddate) values(?, ?, ?, ?)", 
        (user[0], form["toolid"].value, form["inputDate"].value, strdate))

        DB.commitAndCloseConnection(conn)
    
    # adding invoice records depending on choosed options by user
    @staticmethod
    def addInvoiceRecord(form, dispatch=False, lateReturn=False, lateReturnFee=0):
        conn = DB.createConnection()
        c = conn.cursor()
        user = DB.getCurrUserData()
        if lateReturn:
            c.execute("insert into invoices(userid, toolid, toolname, price, dateofrent) values (?, ?, ?, ?, ?)",
            (user[0], form["toolid"].value, "Late return of tool fine", lateReturnFee, datetime.now().strftime('%Y-%m-%d')))
            pass
        if dispatch:
            c.execute("insert into invoices(userid, toolid, toolname, price, dateofrent) values (?, ?, ?, ?, ?)",
            (user[0], form["toolid"].value, "Dispatch of a tool", 10, datetime.now().strftime('%Y-%m-%d')))    
        else:
            c.execute("insert into invoices(userid, toolid, toolname, price, dateofrent) values (?, ?, ?, ?, ?)",
             (user[0], form["toolid"].value, form["inputName"].value, int(form["inputPrice"].value) * int(float(form["inputSelect"].value)), form["inputDate"].value))
            c.execute("insert into invoices(userid, toolid, toolname, price, dateofrent) values (?, ?, ?, ?, ?)",
            (user[0], form["toolid"].value, "Insurance for a tool", 5, datetime.now().strftime('%Y-%m-%d')))
        DB.commitAndCloseConnection(conn)

    # copying selected file by user to specified directory and returning file name
    @staticmethod
    def copyFileToDir(form, dirpath):
        #shutil.copy2(filePath, dirpath)
        if "inputFile" not in form: return
        fileitem = form["inputFile"]        
        if not fileitem.file: return
        if fileitem.filename == "": return
        outpath = os.path.join(dirpath, fileitem.filename)

        with open(outpath, 'wb') as fout:
            shutil.copyfileobj(fileitem.file, fout, 100000)
        return fileitem.filename        
    
    # changing values in database after user returned a tool
    @staticmethod
    def makeToolReturned(form):
        imgName = DB.copyFileToDir(form, os.getcwd() + "/gui/returnedTools_img/")
        conn = DB.createConnection()
        c = conn.cursor()
        today = datetime.now().strftime('%Y-%m-%d')
        user = DB.getCurrUserData()
        c.execute("select * from booked_tools where userid=? and ? >= startdate and returned=0 and toolid=?" , (user[0], today, form["toolid"].value))
        toolToReturn = c.fetchall()[0]      
        returnDate = datetime.strptime(toolToReturn[4], "%Y-%m-%d")
        c.execute("select * from tools where id=?", (form["toolid"].value,))
        tool = c.fetchall()[0]
        pricePerDay = tool[5]
        
        # checking if user is not late with return if is then add fee for late return
        if datetime.now() > returnDate:            
            datediff = abs((today, returnDate).days)
            priceToPay = datediff * pricePerDay
            DB.addInvoiceRecord(form, False, True, priceToPay)
            pass
        c.execute("update booked_tools set returned=1 where userid=? and toolid=? and ? between startdate and enddate",
         (user[0], form["toolid"].value, datetime.now().strftime('%Y-%m-%d')))
        #add record to rented tools database
        c.execute("insert into returned_tools(ownerid, userid, toolid, picname, condition) values(?, ?, ?, ?, ?)",
         (tool[4],user[0], tool[0], imgName, form["inputCondition"].value))
        DB.commitAndCloseConnection(conn)
        pass

    # adding new records to database after user adds a new tool
    @staticmethod
    def addNewTool(form):
        img = DB.copyFileToDir(form, os.getcwd() + "/gui/img/")
        conn = DB.createConnection()
        c = conn.cursor()
        user = DB.getCurrUserData()
        c.execute("insert into tools(toolname, tooldesc, imagename, ownerid, price, avilabile, dateavilabile) values(?, ?, ?, ?, ?, ?, ?)",
         (form["inputNewToolName"].value, form["inputNewToolDesc"].value, img, user[0], form["inputPrice"].value, 1, form["inputDate"].value))
        DB.commitAndCloseConnection(conn)
        pass