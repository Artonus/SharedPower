
import cgi
import cgitb
import os
import sqlite3
import sys
from sqlite3 import Error

#sys.path.append('../')
from classes.template import Template
from core.database import DB

cgitb.enable()
# import classes.template.Template
# import core.user.User

def main():
    currUser = DB.getCurrUser()
    conn = DB.create_connection()
    t = Template()
    form = cgi.FieldStorage()        
    if conn != None:
        c = conn.cursor()
        c.execute("select * from users where username=?", (currUser,))
        tmp = c.fetchall()
        
        currUserData = tmp[0]
        print('Content-type: text/html')
        print('')

        print(t.getTemplate('head').format(userName=currUser))
        print(t.getTemplate('sidebar'))
        print(t.getTemplate('userPanel').format(username=currUserData[1], email=currUserData[6], name=currUserData[3], surname=currUserData[4], adress=currUserData[5]))

        print(t.getTemplate('toolStart'))

        
        c.execute("select * from tools where owner=?", (currUser,))                
        result = c.fetchall()
        for tool in result:
            print(t.getTemplate('tool').format(toolName=tool[1], toolDesc=tool[2], toolPic=tool[3]))
            #print(tool)
        
        print(t.getTemplate('toolEnd'))
        print(t.getTemplate('foot'))
        conn.close()
        pass        
    

if __name__ == "__main__":
    main()   
