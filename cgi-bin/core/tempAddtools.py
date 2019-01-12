#import database as db
import datetime
import os
import sqlite3
from sqlite3 import Error
#users = db.DB("users")
# print(users.show().__dict__)

conn = sqlite3.connect('{0}\db\{1}.db'.format(os.getcwd(), "sharedpower"))

#tools = db.DB("tools")
#print(str(list(tools.show())
c = conn.cursor()

c.execute("""insert into tools (toolname, tooldesc, ownerid, imagename, price, avilabile, dateavilabile ) values("Lightsaber", "Havely used. I cut with it the legs and hand of this bastard that killed younglings, while having highground.", "1", "logo.svg", 777, 1,""" + str(datetime.datetime.now().date()) + ")")
c.execute("""insert into tools (toolname, tooldesc, ownerid, imagename, price, avilabile, dateavilabile ) values("C3PO", "I hate him take him away.", "2", "logo.svg", 1, 1, """ + str(datetime.datetime.now().date()) + ")")
# tool2 = tool.Tool("Lightsaber", "swords", "Havely used. I cut with it the legs and hand of this bastard that killed younglings, while having highground.", "123", "logo.svg", 777, True, datetime.datetime.now().date())
# tool3 = tool.Tool("C3PO", "droid", "I hate him take him away.", "123", "logo.svg", 1, True, datetime.datetime.now().date())

# tools.add(tool1)
# tools.add(tool2)
# tools.add(tool3)
conn.commit()
conn.close()
# print(tools.show().__dict__)

