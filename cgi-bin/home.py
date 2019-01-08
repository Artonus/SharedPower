
import cgi
import sys
sys.path.append('../')
from sharedpower.classes.template import Template
from sharedpower.core.database import DB
from sharedpower.core.user import User

currUser = None

t = Template()
form = cgi.FieldStorage()

if "inputName" in form and "inpotPassword" in form:
    login(form)
    pass

print('Content-type: text/html')
print('')

print(t.getTemplate('head').format(userName=currUser.username()))
print(t.getTemplate('nav'))
print(t.getTemplate('sidebar'))
print(t.getTemplate('toolStart'))
print(t.getTemplate('tool'))
print(t.getTemplate('toolEnd'))
print(t.getTemplate('foot'))



def login(form):
    db = DB("users")    
    users = db.show()
    hashedPass = db.hash(form["inputPassword"])
    for i in users: #todo: how to get uuid of a user with         
        if i["username"] == form["inputUserName"] and i["password"] == hashedPass:
            currUser = User(form["inputUserName"], hashedPass)
            pass
    if currUser == None:
        currUser = User(form["inputUserName"], hashedPass)
        db.add(db.uuid(), currUser)
        db.save()
        pass
    pass

