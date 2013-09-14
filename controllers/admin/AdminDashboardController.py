from ..BaseController import *

class AdminDashboard(BaseHandler):
    def get(self):
        self.route('/templates/admin/adminDashboard.html')