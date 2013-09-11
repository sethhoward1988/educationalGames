from ..BaseController import *

class AdminHome(BaseHandler):
    def get(self):
        self.route('/templates/admin/adminHome.html')