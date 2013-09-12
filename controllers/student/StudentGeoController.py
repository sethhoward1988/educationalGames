from ..BaseController import *

class StudentGeo(BaseHandler):
    def get(self):
        self.route('/templates/student/studentGeo.html')