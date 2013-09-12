from ..BaseController import *

class PublicMission(BaseHandler):
    def get(self):
        self.route('/templates/public/publicMission.html', True)