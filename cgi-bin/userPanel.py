
import cgi
import cgitb
import os
import sqlite3
import sys
from sqlite3 import Error

from core.template import Template
from core.database import DB

cgitb.enable()
form = cgi.FieldStorage() 

def main():
    currUser = DB.getCurrUser()
    conn = DB.createConnection()
    t = Template()
    # printing of a user data panel and tools owned by current user
    if conn != None:
        c = conn.cursor()
        c.execute("select * from users where username=?", (currUser,))
        tmp = c.fetchall()        
        currUserData = list(tmp[0])
        print('Content-type: text/html')
        print('')

        print(t.getTemplate('head').format(userName=currUser))
        print(t.getTemplate('sidebar'))
        if not currUserData[3]:
            currUserData[3] = ""
        if not currUserData[4]:
            currUserData[4] = ""
        if not currUserData[5]:
            currUserData[5] = ""
        if not currUserData[6]:
            currUserData[6] = ""
        print(t.getTemplate('userPanel').format(username=currUserData[1], email=currUserData[6], name=currUserData[3], surname=currUserData[4], adress=currUserData[5])) # filling templates with correct data

        print(t.getTemplate('toolStart'))

        c.execute("select * from tools where ownerid=? and avilabile=1", (currUserData[0],))
        result = c.fetchall()
        for tool in result:
            print(t.getTemplate('tool2').format(id=tool[0], toolName=tool[1], toolDesc=tool[2], toolPic=tool[3], price=tool[5])) # filling templates with correct data        
        
        print(t.getTemplate('toolEnd'))
        print(t.getTemplate('foot'))
        conn.close()
        pass        

def deleteTool(): # function does not delete a tool, it makes it invisible so invoices can still be made using this tool
    conn = DB.createConnection()
    c = conn.cursor()
    c.execute("update tools set avilabile =0 where id=?", (form["toolid"].value,))
    conn.commit()
    conn.close()
    pass
# function to update user details after clicking 'Submit Changes' button and apply them to database
def updateUserDetails():
    conn = DB.createConnection()  
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
    # checking if user wants to delete a tool
    if "toolid" in form:
        deleteTool()
    # checking if user updates his personal data
    if "inputEmail" in form or "inputName" in form:
        updateUserDetails()        
    main()
