import webapp2

from google.appengine.api import users

# Import Error Handlers
from controllers.ErrorController import *

# Superintendent Controllers
from controllers.superintendent.SuperintendentHomeController import *
from controllers.superintendent.SuperintendentSetupController import *
from controllers.superintendent.SuperintendentEditSchool import *
from controllers.superintendent.SuperintendentEditClass import *

# Import Classes
from models.Person import *
from models.School import *
from models.Game import *

print "Running Superintendent Routes"

current_user = users.get_current_user()
query = Person.query(Person.user_id == current_user.user_id())
person = query.fetch(1)
try:
    current_person = person[0]
except:
    current_person = False
if current_person == False or 'superintendent' not in current_person.role:
    app = webapp2.WSGIApplication([(r'/superintendent/.*', GoHome)],debug=True)
else:
    config = {}
    config['webapp2_extras.sessions'] = {
        'secret_key': 'some-secret-key',
        'current_person': current_person,
        'current_user': current_user
    }

    app = webapp2.WSGIApplication([
        # Superintendent Routes
		(r'/superintendent/home', SuperintendentHome),
		(r'/superintendent/setup', SuperintendentSetup),
		(r'/superintendent/setup/(.+)', SuperintendentEditSchool),      # School ID
		(r'/superintendent/setup/(.+)/(.+)', SuperintendentEditClass), # School ID, Class ID
    ], debug=True, config = config)
    app.error_handlers[404] = handle_404
    app.error_handlers[500] = handle_500




