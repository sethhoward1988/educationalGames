from ..BaseController import *

class StudentHome(BaseHandler):
    def get(self):
        self.route('/templates/student/studentHome.html')