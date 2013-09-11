from BaseController import BaseHandler

class EditSchool(BaseHandler):
    def get(self, school_id):
        self.route('/templates/admin/adminEditSchool.html')