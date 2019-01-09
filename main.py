
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

def logging():
    curdatetime = datetime.datetime.now().strftime('%y-%m-%d-%H-%M')
    logfile = str('{0}\log\{1}.log'.format(os.getcwd(), curdatetime))
    buffer = 1
    sys.stderr = open(logfile, 'w', buffer)

def main():
    os.chdir(working)
    server = HTTPServer(address, CGIHTTPRequestHandler)
    #logging()
    createDatabase()
    server.serve_forever()

def createDatabase():
    try:
        conn = sqlite3.connect('{0}\db\{1}.db'.format(os.getcwd(), "sharedpower"))
        print(sqlite3.version)
        if conn is not None:
            c = conn.cursor()        
            c.execute(Scripts.dbScripts.usersTableSql())
            c.execute(Scripts.dbScripts.toolsTableSql())
            # c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            # print(c.fetchall())
            pass
    except Error as e:
        print(e)
    finally:
        conn.close()
    pass
if __name__ == "__main__":
    main()   
