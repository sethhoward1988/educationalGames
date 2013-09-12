from ..BaseController import *

class SuperintendentHome(BaseHandler):
    def get(self):
        self.route('/templates/superintendent/superintendentHome.html')