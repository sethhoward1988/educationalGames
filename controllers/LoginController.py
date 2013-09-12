from BaseController import *

class Login(BaseHandler):
    def get(self):
        user = users.get_current_user()
        self.session.clear()
        self.redirect(users.create_login_url('/'))