from ..BaseController import *

class SpellingPage(BaseHandler):
    def get(self):
        self.route('/templates/user/userSpelling.html')