from ..BaseController import *

class StudentAccount(BaseHandler):
    def get(self):
        self.route('/templates/student/studentAccount.html')

    def getTemplateValues(self, user):
        return { 
            'role': '',
            'nickname': user.nickname(),
            'email': user.email()
        }