from BaseController import *

class Login(BaseHandler):
    def get(self):
        user = users.get_current_user()
        print user
        if user:
            self.baseRedirect()
        else:
            self.session.clear()
            self.redirect(users.create_login_url('/'))