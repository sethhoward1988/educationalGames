from BaseController import BaseHandler

class AdminSetup(BaseHandler):
    def get(self):
        self.route('/templates/admin/setup.html')