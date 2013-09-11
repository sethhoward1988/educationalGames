import webapp2

# Public View
from controllers.public.PublicHomeController import PublicHome
from controllers.public.PublicAboutController import PublicAbout
from controllers.public.PublicMissionController import PublicMission
from controllers.public.PublicRegisterController import PublicRegister

# Student View
from controllers.user.MainPageController import MainPage
from controllers.user.GeoController import GeoPage
from controllers.user.SpellingController import SpellingPage
from controllers.user.MathController import MathPage
from controllers.user.ResultsController import Results
from controllers.user.AccountController import Account
from controllers.user.GameController import Game
from controllers.user.LogoutController import Logout

# Teachers View
from controllers.teacher.TeacherHomeController import TeacherHome

# Administration View
from controllers.admin.AdminHomeController import AdminHome
from controllers.admin.AdminSetup import AdminSetup
from controllers.admin.AdminSchool import School
from controllers.admin.AdminClass import Class

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
    (r'/student/geo', GeoPage),
    (r'/student/spelling', SpellingPage),
    (r'/student/math', MathPage),
    (r'/student/results', Results),
    (r'/student/account', Account),
    (r'/student/game', Game),
    
    # Generic Logout
    (r'/logout', Logout),

    # Admin Routes
    (r'/admin/', AdminHome),
    (r'/admin/setup', AdminSetup),
    (r'/admin/setup/school=(\d+)', EditSchool),
    (r'/admin/setup/school=(\d+)/class=(\d+)', EditClass),

    # Teacher Routes
    (r'/teacher/', TeacherHome)

], debug=True, config = config)




