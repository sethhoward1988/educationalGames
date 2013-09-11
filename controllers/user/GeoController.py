from ..BaseController import *

class GeoPage(BaseHandler):
    def get(self):
        self.route('/templates/user/userGeo.html')