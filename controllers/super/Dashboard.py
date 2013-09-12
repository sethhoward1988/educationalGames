from ..BaseController import *

class Dashboard(BaseHandler):
    def get(self):
        self.route('/templates/teacher/teacherHome.html')