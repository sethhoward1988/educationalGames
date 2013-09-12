from ..BaseController import *

class StudentMath(BaseHandler):
    def get(self):
        self.route('/templates/student/studentMath.html')