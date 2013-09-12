import webapp2

# Public Controllers
from controllers.public.PublicHomeController import *
from controllers.public.PublicAboutController import *
from controllers.public.PublicMissionController import *
from controllers.public.PublicRegisterController import *

# Student Controllers
from controllers.user.MainPageController import *
from controllers.user.GeoController import *
from controllers.user.SpellingController import *
from controllers.user.MathController import *
from controllers.user.ResultsController import *
from controllers.user.AccountController import *
from controllers.user.GameController import *

# Generic Controllers
from controllers.LogoutController import *
from controllers.LoginController import *
from controllers.SignUpController import *

# Teachers Controllers
from controllers.teacher.TeacherHomeController import *

# Administration Controllers
from controllers.admin.AdminHomeController import *
from controllers.admin.AdminSetupController import *
from controllers.admin.AdminEditSchool import *
from controllers.admin.AdminEditClass import *

# Super Administration Controllers
from controllers.super.Dashboard import *

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

    # Student Routes
    (r'/student', MainPage),
    (r'/student/geo', GeoPage),
    (r'/student/spelling', SpellingPage),
    (r'/student/math', MathPage),
    (r'/student/results', Results),
    (r'/student/account', Account),
    (r'/student/game', Game),
    
    # Generic Routes
    (r'/logout', Logout),
    (r'/login', Login),
    (r'/signup/userid=(\d)', Signup),

    # Admin Routes
    (r'/admin', AdminHome),
    (r'/admin/setup', AdminSetup),
    (r'/admin/setup/school=(\d+)', EditSchool),
    (r'/admin/setup/school=(\d+)/class=(\d+)', EditClass),

    # Super Admin Routes
    (r'/super/dashboard', Dashboard),

    # Teacher Routes
    (r'/teacher', TeacherHome)

], debug=True, config = config)




