from ..BaseController import *

class SuperintendentSetup(BaseHandler):
    def get(self):
        self.route('/templates/superintendent/superintendentSetup.html')