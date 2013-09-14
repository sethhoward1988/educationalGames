import webapp2

# Public Controllers
from controllers.public.PublicHomeController import *
from controllers.public.PublicAboutController import *
from controllers.public.PublicMissionController import *
from controllers.public.PublicRegisterController import *

# Generic Controllers
from controllers.LogoutController import *
from controllers.LoginController import *
from controllers.SignUpController import *
from controllers.RedirectController import *

# Import Classes
from models.Person import *
from models.Score import *

print "Running Public Routes"

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'some-secret-key',
}

app = webapp2.WSGIApplication([

    # Public Routes
    (r'/', PublicHome),
    (r'/about', PublicAbout),
    (r'/mission', PublicMission),
    (r'/register', PublicRegister),

    # Generic Routes
    (r'/logout', Logout),
    (r'/login', Login),
    (r'/signup/(.+)', Signup),  # User ID
    (r'/signup', SignupPost),
    (r'/redirect', Redirect)

], debug=True, config = config, )
