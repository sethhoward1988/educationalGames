from BaseController import BaseHandler

class AdminHome(BaseHandler):
    def get(self):
        self.route('/templates/admin/home.html')