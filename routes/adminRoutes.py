import webapp2

from google.appengine.api import users

# Import Error Handlers
from controllers.ErrorController import *

# Super Administration Controllers
from controllers.admin.AdminDashboardController import *

# Import Classes
from models.Person import *
from models.School import *
from models.Game import *

print "Running Admin Route"

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'some-secret-key'
}

print "Running Admin App"

app = webapp2.WSGIApplication([

    # Super Admin Routes
    (r'/admin/home', AdminDashboard)

], debug=True, config = config)




