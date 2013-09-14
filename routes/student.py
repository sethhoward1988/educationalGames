import webapp2

from google.appengine.api import users

# Import Error Handlers
from controllers.ErrorController import *

# Student Controllers
from controllers.student.StudentAccountController import *
from controllers.student.StudentGameController import *
from controllers.student.StudentGeoController import *
from controllers.student.StudentHomeController import *
from controllers.student.StudentMathController import *
from controllers.student.StudentResultsController import *
from controllers.student.StudentSpellingController import *

# Import Classes
from models.Person import *
from models.School import *
from models.Game import *

print "Running Student routes"

current_user = users.get_current_user()
query = Person.query(Person.user_id == current_user.user_id())
person = query.fetch(1)
try:
    current_person = person[0]
except:
    current_person = False
if current_person == False or 'student' not in current_person.role:
    app = webapp2.WSGIApplication([(r'/student/.*', GoHome)],debug=True)
else:
    config = {}
    config['webapp2_extras.sessions'] = {
        'secret_key': 'some-secret-key',
        'current_person': current_person,
        'current_user': current_user
    }

    app = webapp2.WSGIApplication([
        (r'/student/home', StudentHome),
        (r'/student/account', StudentAccount),
        (r'/student/geo', StudentGeo),
        (r'/student/math', StudentMath),
        (r'/student/spelling', StudentSpelling),
        (r'/student/results', StudentResults)
    ], debug=True, config = config)
    app.error_handlers[404] = handle_404
    app.error_handlers[500] = handle_500






