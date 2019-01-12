import os
import sys
import time
import datetime
import sqlite3
from sqlite3 import Error
import db.dbScripts as Scripts
from http.server import HTTPServer, CGIHTTPRequestHandler


port = 8888
address = ("", port)
working = os.getcwd()

# logging errors and events by cgi to the file
def logging():
    curdatetime = datetime.datetime.now().strftime('%y-%m-%d-%H-%M')
    logfile = str('{0}\log\{1}.log'.format(os.getcwd(), curdatetime))
    buffer = 1
    sys.stderr = open(logfile, 'w', buffer)
# seting up a server
def main():
    os.chdir(working)
    server = HTTPServer(address, CGIHTTPRequestHandler)
    #logging()
    createDatabase()
    server.serve_forever()
# creating database
def createDatabase():
    try:
        # establishing connection with database and creating it if does not exist
        conn = sqlite3.connect('{0}\db\{1}.db'.format(os.getcwd(), "sharedpower"))
        print(sqlite3.version)
        if conn is not None:
            c = conn.cursor()        
            c.execute(Scripts.dbScripts.usersTableSql())
            c.execute(Scripts.dbScripts.toolsTableSql())
            c.execute(Scripts.dbScripts.invoicesTableSql())
            c.execute(Scripts.dbScripts.booked_toolsTableSql())
            c.execute(Scripts.dbScripts.returned_toolsTableSql())
            conn.commit()            
            pass
    except Error as e:
        print(e)
    finally:
        conn.close()
    pass
if __name__ == "__main__":
    main()   
