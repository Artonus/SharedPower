
import cgi
import sys
#sys.path.append('../')
from classes.template import Template
from core.database import DB
from core.user import User
# import classes.template.Template
# import core.user.User

currUser = None

t = Template()
form = cgi.FieldStorage()
# print("dupa")
if "inputUsername" in form and "inputPassword" in form:    
    db = DB("users")    
    users = db.show()
    #print(users)
    hashedPass = db.hash(form["inputPassword"].value)
    for i in users: #todo: how to get uuid of a user with , fuck uuid!!!!        
        if i[1] == form['inputUsername'] and i[1]["password"] == hashedPass:
            currUser = User(form["inputUserName"], hashedPass)
            pass
    if currUser == None:
        currUser = User(form["inputUsername"].value, hashedPass)
        result = db.add(currUser.username(), currUser.__dict__)
        if result == False:
            print("Can't create an account")
        db.save()
        pass
    print('Content-type: text/html')
    print('')

    print(t.getTemplate('head').format(userName=currUser.username()))
    print(t.getTemplate('nav'))
    print(t.getTemplate('sidebar'))

    print(t.getTemplate('toolStart'))
    dbTools = DB("tools")
    print(t.getTemplate('tool'))
    print(t.getTemplate('toolEnd'))
    print(t.getTemplate('foot'))
 


# dic = {
#     "key": username,
#     "data": {
#        User object
#     }
# }