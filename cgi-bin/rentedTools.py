
import cgi
import cgitb
import os
import sqlite3
import sys
from datetime import datetime
from sqlite3 import Error

from core.template import Template
from core.database import DB

# from .db.dbScripts import dbScripts

cgitb.enable()
form = cgi.FieldStorage()

def main():
    currUser = None
    t = Template()
    conn = DB.createConnection()
    currUser = DB.getCurrUserData()
    # printing panel of currently rented tools by user
    if conn != None:
        print('Content-type: text/html')
        print('')

        print(t.getTemplate('head').format(userName=currUser[1]))
        print(t.getTemplate('sidebar'))
        print(t.getTemplate('toolStart'))
        print('<h3 class="mt-3">Tools you rent</h3>')
        today = datetime.now().strftime('%Y-%m-%d')
        if conn is not None:
            c = conn.cursor()
            # searching for currently rented tools
            c.execute("select * from booked_tools where userid=? and ? >= startdate and returned=0" , (currUser[0], today))
            result = c.fetchall()
            if len(result) == 0:
                print("""<h5 class="mt-3">You currently don't rent any tools</h5>""")
            for bookedTool in result:
                c.execute("select * from tools where id=?", (bookedTool[2],))
                tool = c.fetchall()[0]
                print(t.getTemplate('rentedTool').format(id=tool[0], toolName=tool[1], toolDesc=tool[2], toolPic=tool[3], price=tool[5]))
            pass
        print(t.getTemplate('toolEnd'))
        print(t.getTemplate('foot'))
        conn.close()
        pass
# function recieving a value form form to retun a tool and calling database to write changes
def returnTool():    
    if form.getvalue("inputDispatch", '').lower() in ['true', 'yes','t', '1', 'on', 'checked']:
        DB.addInvoiceRecord(form, True)
    DB.makeToolReturned(form)
    pass

if __name__ == "__main__":
    # checking if returning a tool form was filled
    if "inputName" in form and "inputDesc" in form:
        returnTool()
    main()
