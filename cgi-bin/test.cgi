#!/usr/bin/ python3

import cgi
import sys
import os
sys.path.appened('../')
#from sharedpower.classes.template import Template

#t = Template()
form = cgi.FieldStorage()

print('Content-type: text/html')
print('')

print('hello')

#print(t.getTemplate('head'))
#print(t.getTemplate('nav'))
#print(t.get('sidebar'))
#print(t.getPage('home'))
#print(t.getTemplate('foot'))
