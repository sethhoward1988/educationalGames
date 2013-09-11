from BaseController import BaseHandler

class Account(BaseHandler):
    def get(self):
        self.route('/templates/account.html')

    def getTemplateValues(self, user):
        return { 
            'role': self.session['user_role'],
            'nickname': user.nickname(),
            'email': user.email()
        }