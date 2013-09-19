import webapp2

from google.appengine.api import users

# Import Error Handlers
from controllers.ErrorController import *

# Principals Controllers
from controllers.principal.PrincipalHomeController import *
from controllers.principal.PrincipalEditAccountController import *
from controllers.principal.PrincipalRelieveController import *
from controllers.principal.PrincipalEditSchoolController import *
from controllers.principal.PrincipalAddClassController import *
from controllers.principal.PrincipalGetClassController import *

# Import Classes
from models.Person import *
from models.School import *
from models.Game import *

print "Running Principal Routes"

current_user = users.get_current_user()
query = Person.query(Person.user_id == current_user.user_id())
person = query.fetch(1)

try:
    current_person = person[0]
except:
    current_person = False
if current_person == False or 'principal' not in current_person.role:
    app = webapp2.WSGIApplication([(r'/principal/.*', GoHome)],debug=True)
else:
    query = School.query(School.administrator == current_person.key)
    school = query.fetch(1)[0]
    config = {}
    config['webapp2_extras.sessions'] = {
        'secret_key': 'some-secret-key',
        'current_person': current_person,
        'current_user': current_user,
        'school': school
    }

    app = webapp2.WSGIApplication([
        # Teacher Routes
    	(r'/principal/home', PrincipalHome)
        (r'/principal/account', PrincipalEditAccount),
        (r'/principal/relieve', PrincipalRelieve),
        (r'/principal/school', PrincipalEditSchool),
        (r'/principal/class', PrincipalAddClass)
        (r'/principal/class/(.+)', PrincipalGetClass), # class guid

    ], debug=True, config = config)
    app.error_handlers[404] = handle_404
    app.error_handlers[500] = handle_500




