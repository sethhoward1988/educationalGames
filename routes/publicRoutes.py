import webapp2

# Import Error Handlers
from controllers.ErrorController import *

# Public Controllers
from controllers.public.PublicHomeController import *
from controllers.public.PublicProductController import *
from controllers.public.PublicAboutController import *
from controllers.public.PublicMissionController import *
from controllers.public.PublicContactController import *

# Generic Controllers
from controllers.LogoutController import *
from controllers.LoginController import *
from controllers.SignUpController import *
from controllers.RedirectController import *

# Populate DB 
from controllers.Populate import *

# Import Classes
from models.Person import *
from models.School import *
from models.Game import *

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
    (r'/product', PublicProduct),
    (r'/contact', PublicContact),
    (r'/populate', Populate),

    # Generic Routes
    (r'/logout', Logout),
    (r'/login', Login),
    (r'/signup/(.+)', Signup),  # User ID
    # (r'/signup', SignupPost),
    (r'/redirect', Redirect)

    # json calls
    # (r'/person', PersonController),
    # (r'/district', DistrictController),
    # (r'/school', SchoolController),
    # (r'/class', ClassController),
    # (r'/game', GameController)

], debug=True, config = config, )

app.error_handlers[404] = handle_404
app.error_handlers[500] = handle_500
