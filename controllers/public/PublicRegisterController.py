from ..BaseController import *

class PublicRegister(BaseHandler):
    def get(self):
        self.route('/templates/public/publicRegister.html', True)