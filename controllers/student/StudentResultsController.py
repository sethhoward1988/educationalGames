from ..BaseController import *

class StudentResults(BaseHandler):
    def get(self):
        self.route('/templates/student/studentResults.html')