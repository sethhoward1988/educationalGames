from ..BaseController import *

class Results(BaseHandler):
    def get(self):
        self.route('/templates/user/userResults.html')