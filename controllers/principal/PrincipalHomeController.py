from ..BaseController import *

class PrincipalHome(BaseHandler):
    def get(self):
        self.route('/templates/principal/principalHome.html')