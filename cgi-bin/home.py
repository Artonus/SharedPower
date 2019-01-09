
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
    currUser = None
    t = Template()
    form = cgi.FieldStorage()
        
    if "inputUsername" in form and "inputPassword" in form:            
        conn = DB.create_connection()
        hashedPass = DB.hash(form["inputPassword"].value)
        if conn != None:
            try:
                c = conn.cursor()
                c.execute("select * from users where username=? and password=?", (form["inputUsername"].value, hashedPass))
                rows = c.fetchall()
                if len(rows) == 1:
                    currUser = rows[0]
                else:
                    currUser = None

            except Error as e:
                print(e)
            pass    
        if currUser is None:
            # try:
                c = conn.cursor()
                c.execute("insert into users(username, password) values(?, ?)", (form["inputUsername"].value, hashedPass))
                #conn.commit()
                #userId = c.lastrowid
                c.execute("select * from users where username=? and password=?", (form["inputUsername"].value, hashedPass))
                rows = c.fetchall()
                currUser = rows[0]
                conn.commit()
            # except Error as e:
            #     print(e)
                pass
        DB.setCurrUser(currUser)
        if conn != None:
            print('Content-type: text/html')
            print('')

            print(t.getTemplate('head').format(userName=currUser[1]))
            #print(t.getTemplate('nav'))
            print(t.getTemplate('sidebar'))
            print(t.getTemplate('toolStart'))
            if conn is not None:
                c = conn.cursor()
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
    pass

if __name__ == "__main__":
    main()   
