from ..BaseController import *

class StudentSpelling(BaseHandler):
    def get(self):
        self.route('/templates/student/studentSpelling.html')