
import cgi
import cgitb
import os
import sqlite3
import sys
from datetime import datetime
from sqlite3 import Error

from classes.template import Template
from core.database import DB

# from .db.dbScripts import dbScripts

cgitb.enable()
form = cgi.FieldStorage()

def main():
    currUser = None
    t = Template()
    conn = DB.create_connection()
    currUser = DB.getCurrUserData()
    if conn != None:
        print('Content-type: text/html')
        print('')

        print(t.getTemplate('head').format(userName=currUser[1]))
        print(t.getTemplate('sidebar'))
        print(t.getTemplate('toolStart'))
        today = datetime.now().strftime('%Y-%m-%d')
        if conn is not None:            
            c = conn.cursor()            
            c.execute("select * from booked_tools where userid=? and ? between startdate and enddate", (currUser[0], today))
            result = c.fetchall()
            for rentedTool in result:
                c.execute("select * from tools where id=?", (rentedTool[2]))
                tool = c.fetchall()[0]
                print(t.getTemplate('rentedTool').format(id=tool[0], toolName=tool[1], toolDesc=tool[2], toolPic=tool[3], price=tool[5]))
            pass
        print(t.getTemplate('toolEnd'))
        print(t.getTemplate('foot'))
        conn.close()
        pass        

if __name__ == "__main__":
    if "inputSelect" in form and "inputDate" in form:
        DB.addBookedTool(form)
        pass
    main()   
