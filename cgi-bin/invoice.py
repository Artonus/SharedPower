
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
        print(t.getTemplate('invoiceStart'))
        
        c.execute("select * from invoices where userid=?", (currUserData[0],))                
        result = c.fetchall()
        sumOfPayments=0
        num=-1
        for payment in result:
            num+=2            
            sumOfPayments+=payment[4] + 5
            print(t.getTemplate('invoice').format(toolName=payment[3], dateOfRent=payment[5], price=payment[4], rownum=num, rownum2=num+1))            
        num+=2
        print(t.getTemplate('invoiceSumRow').format(priceSum=sumOfPayments, num=num))
        print(t.getTemplate('invoiceEnd'))
        print(t.getTemplate('foot'))
        conn.close()
        pass        
    

if __name__ == "__main__":
    main()   
