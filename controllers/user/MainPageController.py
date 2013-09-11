from BaseController import BaseHandler

class MainPage(BaseHandler):
    def get(self):
        self.route('/templates/home.html')