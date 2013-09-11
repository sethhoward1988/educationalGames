from ..BaseController import *

class MathPage(BaseHandler):
    def get(self):
        self.route('/templates/user/userMath.html')