
import cgi
import cgitb
import os
import shutil
import sqlite3
import sys
from datetime import datetime
from sqlite3 import Error

from core.template import Template
from core.database import DB

cgitb.enable()
form = cgi.FieldStorage() 

def main():
    currUser = DB.getCurrUser()
    conn = DB.createConnection()
    t = Template()
    # printing a form to return a selected tool
    if conn != None:
        c = conn.cursor()
        c.execute("select * from tools where id=?", (form["toolid"].value,))
        tmp = c.fetchall()
        tool = tmp[0]
        print('Content-type: text/html')
        print('')
        print(t.getTemplate('head').format(userName=currUser))
        print(t.getTemplate('sidebar'))
        print(t.getTemplate('returnTool').format(tool[1], tool[2], tool[5],tool[7], form["toolid"].value)) # filling templates with correct data
        print(t.getTemplate('foot'))
        conn.close()
        pass
        
if __name__ == "__main__":
    
    main()
