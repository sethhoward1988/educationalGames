from BaseController import BaseHandler

class Results(BaseHandler):
    def get(self):
        self.route('/templates/results.html')