
import calendar
import cgi
import cgitb
import os
import sqlite3
import sys
from datetime import datetime
from sqlite3 import Error

from core.database import DB
#sys.path.append('../')
from core.template import Template

cgitb.enable()
# import classes.template.Template
# import core.user.User
def formatMonthToInt(string):
    if string[0] == '0':
        return int(string[1])
    return int(string)
def main():
    currUser = DB.getCurrUser()
    conn = DB.createConnection()
    t = Template()
    form = cgi.FieldStorage()    
    # printing panel of invoices    
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
        # getting current month invoices
        now = datetime.now()
        firstDayOfMonth = datetime(now.year, now.month, 1).strftime("%Y-%m-%d")
        
        #stack function for removing 0 from the beginning of month number
        lastDayOfMonth = calendar.monthrange(int(datetime.now().strftime("%Y")), formatMonthToInt(datetime.now().strftime("%m")) )[1]
        c.execute("select * from invoices where userid=? and dateofrent between ? and ?", (currUserData[0], firstDayOfMonth, lastDayOfMonth))
        result = c.fetchall()
        sumOfPayments = 0
        num = 0
        # printing invoices of current user
        for payment in result:
            num += 1            
            sumOfPayments += payment[4]
            print(t.getTemplate('invoice').format(toolName=payment[3], dateOfRent=payment[5], price=payment[4], rownum=num))
        num += 1
        print(t.getTemplate('invoiceSumRow').format(priceSum=sumOfPayments, num=num))
        print(t.getTemplate('invoiceEnd'))
        print(t.getTemplate('foot'))
        conn.close()
        pass
    

if __name__ == "__main__":
    main()   
