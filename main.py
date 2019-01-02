#!/usr/bin/ python

import os
import sys
import time
import datetime
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8080
address = ('', port)
working = '.' #os.getcwd()

def logging():
    curdatetime = datetime.datetime.now().strftime('%y-%m-%d-%H-%M')
    logfile = str('{0}\log\{1}.log'.format(os.getcwd(), curdatetime))
    buffer = 1
    sys.stderr = open(logfile, 'w', buffer)

def main():
    os.chdir(working)
    server = HTTPServer(address, CGIHTTPRequestHandler)
    #logging()
    server.serve_forever()

if __name__ == "__main__":
    main()
