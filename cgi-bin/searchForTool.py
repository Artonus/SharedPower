
import cgi
import cgitb
import os
import sqlite3
import sys
from sqlite3 import Error

#sys.path.append('../')
from classes.template import Template
from core.database import DB
from core.user import User

cgitb.enable()
# import classes.template.Template
# import core.user.User

def main():
    currUser = None
    t = Template()
    form = cgi.FieldStorage()        
    conn = DB.create_connection()
    if conn != None:
        print('Content-type: text/html')
        print('')

        print(t.getTemplate('head'))#.format(userName=DB.currUser[1]))
        print(t.getTemplate('sidebar'))
        print(t.getTemplate('toolStart'))
        if conn is not None:            
            c = conn.cursor()
            if "search" in form:
                c.execute("select * from tools where avilabile=1 and toolname like ? ", ("'&"+form["search"].value+"%'",))
                pass
            else:
                c.execute("select * from tools where avilabile=1")                
            result = c.fetchall()
            for tool in result:
                print(t.getTemplate('tool').format(toolName=tool[1], toolDesc=tool[2], toolPic=tool[3]))
                #print(tool)
            pass    
        print(t.getTemplate('toolEnd'))
        print(t.getTemplate('foot'))
        conn.close()
        pass        
    

if __name__ == "__main__":
    main()   
