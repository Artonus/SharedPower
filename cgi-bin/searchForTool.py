
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
form = cgi.FieldStorage()

def main():
    currUser = None
    t = Template()
    conn = DB.create_connection()
    currUser = DB.getCurrUser()
    if conn != None:
        print('Content-type: text/html')
        print('')

        print(t.getTemplate('head').format(userName=currUser))
        print(t.getTemplate('sidebar'))
        print(t.getTemplate('toolStart'))
        if conn is not None:            
            c = conn.cursor()
            if "search" in form:
                c.execute("select * from tools where avilabile=1 and toolname like ? ", ("%"+form["search"].value+"%",))
                pass
            else:
                c.execute("select * from tools where avilabile=1")                
            result = c.fetchall()
            for tool in result:
                print(t.getTemplate('tool').format(id=tool[0], toolName=tool[1], toolDesc=tool[2], toolPic=tool[3], price=tool[5]))
                #print(tool)
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
