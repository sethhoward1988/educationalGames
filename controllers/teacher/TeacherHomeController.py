from ..BaseController import *

class TeacherHome(BaseHandler):
    def get(self):
        self.route('/templates/teacher/teacherHome.html')