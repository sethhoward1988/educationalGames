from BaseController import *

class Signup(BaseHandler):
    def get(self, user_id):
        self.route('/templates/signup.html')