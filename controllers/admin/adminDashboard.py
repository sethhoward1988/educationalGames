from ..BaseController import *

class SuperadminDashboard(BaseHandler):
    def get(self):
        self.route('/templates/superadmin/superadminDashboard.html')