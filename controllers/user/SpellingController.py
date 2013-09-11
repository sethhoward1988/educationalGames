from BaseController import BaseHandler

class SpellingPage(BaseHandler):
    def get(self):
        self.route('/templates/spelling.html')