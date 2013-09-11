from ..BaseController import *

class MainPage(BaseHandler):
    def get(self):
        self.route('/templates/user/userHome.html')