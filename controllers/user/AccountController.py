from ..BaseController import *

class Account(BaseHandler):
    def get(self):
        self.route('/templates/user/userAccount.html')

    def getTemplateValues(self, user):
        return { 
            'role': self.session['user_role'],
            'nickname': user.nickname(),
            'email': user.email()
        }