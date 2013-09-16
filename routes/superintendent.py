import webapp2

from google.appengine.api import users

# Import Error Handlers
from controllers.ErrorController import *

# Superintendent Controllers
from controllers.superintendent.SuperintendentHomeController import *
from controllers.superintendent.SuperintendentAddSchoolController import *
from controllers.superintendent.SuperintendentEditSchoolController import *
from controllers.superintendent.SuperintendentAccountController import *

# Import Classes
from models.Person import *
from models.School import *
from models.Game import *

print "Running Superintendent Routes"

current_user = users.get_current_user()
print current_user
query = Person.query(Person.user_id == current_user.user_id())
person = query.fetch(1)
print person
try:
    current_person = person[0]
except:
    current_person = False
if current_person == False or 'superintendent' not in current_person.role:
    app = webapp2.WSGIApplication([(r'/superintendent/.*', GoHome)],debug=True)
else:
    query = School_District.query(School_District.administrator == current_person.key)
    school_district = query.fetch(1)[0]
    config = {}
    config['webapp2_extras.sessions'] = {
        'secret_key': 'some-secret-key',
        'current_person': current_person,
        'current_user': current_user,
        'school_district': school_district
    }

    app = webapp2.WSGIApplication([
        # Superintendent Routes
		(r'/superintendent/home', SuperintendentHome),
        (r'/superintendent/account', SuperintendentAccount),
		(r'/superintendent/school', SuperintendentAddSchool),
		(r'/superintendent/school/(.+)', SuperintendentEditSchool), # School ID
    ], debug=True, config = config)
    app.error_handlers[404] = handle_404
    app.error_handlers[500] = handle_500




