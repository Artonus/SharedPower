
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
# import classes.template.Template
# import core.user.User

def main():
    currUser = DB.getCurrUser()
    conn = DB.create_connection()
    t = Template()
           
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

        c.execute("select * from tools where owner=? and avilabile=1", (currUser,))                
        result = c.fetchall()
        for tool in result:
            print(t.getTemplate('tool2').format(id=tool[0], toolName=tool[1], toolDesc=tool[2], toolPic=tool[3], price=tool[5]))
            #print(tool)
        
        print(t.getTemplate('toolEnd'))
        print(t.getTemplate('foot'))
        conn.close()
        pass        

def deleteTool(): # function does not delete a tool, it makes it invisible so invoices can still be made using this tool
    conn = DB.create_connection()
    c = conn.cursor()
    c.execute("update tools set avilabile =0 where id=?", (form["toolid"].value,))
    conn.commit()
    conn.close()
    pass

def updateUserDetails():
    conn = DB.create_connection()  
    currUser = DB.getCurrUser()  
    c = conn.cursor()
    c.execute("select * from users where username=?", (currUser,))
    userId = c.fetchall()[0][0]
    if "inputPassword" in form:
        hashedPass = DB.hash(form["inputPassword"].value)
        c.execute("update users set password=?, firstname =?, lastname=?, adress=?, email=? where id=?", (hashedPass, form["inputName"].value, form["inputSurname"].value, form["inputAdress"].value, form["inputEmail"].value, userId))        
    else:
        c.execute("update users set firstname=?, lastname=?, adress=?, email=? where id=?", (form["inputName"].value, form["inputSurname"].value, form["inputAdress"].value, form["inputEmail"].value, userId))
    conn.commit()
    conn.close()        
    pass
    
if __name__ == "__main__":
    if "toolid" in form: # check if user wanted to delete a tool
        deleteTool()
    if "inputEmail" in form or "inputName" in form:
        updateUserDetails()        
    main()
