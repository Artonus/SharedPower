
import cgi
import cgitb
import os
import sqlite3
import sys
from sqlite3 import Error
from datetime import datetime

from core.template import Template
from core.database import DB

cgitb.enable()
form = cgi.FieldStorage() 

def main():
    currUser = DB.getCurrUser()
    conn = DB.createConnection()
    t = Template()
    # printing add tool page
    if conn != None:
        c = conn.cursor()        
        print('Content-type: text/html')
        print('')
        print(t.getTemplate('head').format(userName=currUser))
        print(t.getTemplate('sidebar'))
        print(t.getTemplate('addTool'))
        print(t.getTemplate('foot'))
        conn.close()
        pass

if __name__ == "__main__":
    main()
