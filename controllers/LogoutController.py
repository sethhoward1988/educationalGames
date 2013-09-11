from BaseController import *

class Logout(BaseHandler):
    def get(self):
        user = users.get_current_user()
        self.session.clear()
        self.redirect(users.create_logout_url('/'))