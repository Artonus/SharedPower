
import cgi
import sys
sys.path.append('../')
from sharedpower.classes.template import Template

t = Template()
form = cgi.FieldStorage()

print('Content-type: text/html')
print('')

print(t.getTemplate('head'))
print(t.getTemplate('nav'))
#print(t.get('sidebar'))
print(t.getPage('home'))
print(t.getTemplate('foot'))