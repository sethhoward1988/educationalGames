from BaseController import BaseHandler

class MathPage(BaseHandler):
    def get(self):
        self.route('/templates/math.html')