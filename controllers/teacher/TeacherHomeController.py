from BaseController import BaseHandler

class GeoPage(BaseHandler):
    def get(self):
        self.route('/templates/teacher/home.html')