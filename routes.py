import webapp2

# Public Controllers
from controllers.public.PublicHomeController import *
from controllers.public.PublicAboutController import *
from controllers.public.PublicMissionController import *
from controllers.public.PublicRegisterController import *

# Student Controllers
from controllers.student.StudentHomeController import *
from controllers.student.StudentGeoController import *
from controllers.student.StudentSpellingController import *
from controllers.student.StudentMathController import *
from controllers.student.StudentResultsController import *
from controllers.student.StudentAccountController import *
from controllers.student.StudentGameController import *

# Generic Controllers
from controllers.LogoutController import *
from controllers.LoginController import *
from controllers.SignUpController import *

# Teachers Controllers
from controllers.teacher.TeacherHomeController import *

# Principals Controllers
from controllers.principal.PrincipalHomeController import *

# Administration Controllers
from controllers.superintendent.SuperintendentHomeController import *
from controllers.superintendent.SuperintendentSetupController import *
from controllers.superintendent.SuperintendentEditSchool import *
from controllers.superintendent.SuperintendentEditClass import *

# Super Administration Controllers
from controllers.superadmin.SuperadminDashboard import *

# Import Classes
from models.Person import *
from models.Score import *

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

    # Student Routes
    (r'/student', StudentHome),
    (r'/student/geo', StudentGeo),
    (r'/student/spelling', StudentSpelling),
    (r'/student/math', StudentMath),
    (r'/student/results', StudentResults),
    (r'/student/account', StudentAccount),
    (r'/student/game', StudentGame),

    # Principal Routes
    (r'/principal', PrincipalHome),

    # Superintendent Routes
    (r'/superintendent', SuperintendentHome),
    (r'/superintendent/setup', SuperintendentSetup),
    (r'/superintendent/setup/(.+)', SuperintendentEditSchool),      # School ID
    (r'/superintendent/setup/(.+)/(.+)', SuperintendentEditClass), # School ID, Class ID

    # Super Admin Routes
    (r'/superadmin', SuperadminDashboard),

    # Teacher Routes
    (r'/teacher', TeacherHome)

], debug=True, config = config, )




