from ..BaseController import *

class SuperintendentEditClass(BaseHandler):
    def get(self, school_id, class_id):
        self.route('/templates/superintendent/superintendentEditClass.html')