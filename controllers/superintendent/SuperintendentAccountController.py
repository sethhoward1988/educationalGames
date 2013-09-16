from ..BaseController import *

class SuperintendentAccount(BaseHandler):
    def get(self):
    	templateOptions = {
            'nickname': users.get_current_user().nickname(),
            'person': self.app.config.get("webapp2_extras.sessions")["current_person"],
        }
        template = JINJA_ENVIRONMENT.get_template('/templates/superintendent/superintendentAccount.html')
        self.response.write(template.render(templateOptions))

    def post(self):
    	current_person = self.app.config.get("webapp2_extras.sessions")["current_person"]
    	current_person.f_name = self.request.get('f_name')
    	current_person.l_name = self.request.get('l_name')
    	current_person.put()
    	self.redirect('/superintendent/home')