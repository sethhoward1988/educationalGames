from BaseController import BaseHandler

class GeoPage(BaseHandler):
    def get(self):
        self.route('/templates/geo.html')