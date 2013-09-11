from ..BaseController import *

class PublicHome(BaseHandler):
    def get(self):
        self.route('/templates/public/publicHome.html')