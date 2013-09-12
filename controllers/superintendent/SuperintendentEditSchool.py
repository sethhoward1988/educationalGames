from ..BaseController import *

class SuperintendentEditSchool(BaseHandler):
    def get(self, school_id):
        self.route('/templates/superintendent/superintendentEditSchool.html')