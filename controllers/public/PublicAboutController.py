from ..BaseController import *

class PublicAbout(BaseHandler):
    def get(self):
        self.route('/templates/public/publicAbout.html')