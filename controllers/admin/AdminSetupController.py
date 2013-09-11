from ..BaseController import *

class AdminSetup(BaseHandler):
    def get(self):
        self.route('/templates/admin/adminSetup.html')