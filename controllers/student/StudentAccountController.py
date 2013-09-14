from ..BaseController import *

class StudentAccount(BaseHandler):
    def get(self):
        self.route('/templates/student/studentAccount.html')

    def getTemplateValues(self, user):

    	
    	
        return { 
            'role': '',
            'nickname': user.f_name + ' ' + user.l_name,
            'email': user.email()
        }