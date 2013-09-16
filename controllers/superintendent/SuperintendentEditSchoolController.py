from ..BaseController import *

class SuperintendentEditSchool(BaseHandler):
    def get(self, guid):
        school = School.query(School.guid == guid).fetch(1)[0]
        templateOptions = {
            'nickname': users.get_current_user().nickname(),
            'school': school
        }
        template = JINJA_ENVIRONMENT.get_template('/templates/superintendent/superintendentEditSchool.html')
        self.response.write(template.render(templateOptions))

    def post(self, guid):
        school = School.query(School.guid == guid).fetch(1)[0]
        school.name = self.request.get('name')
        school.put()
        self.redirect('/superintendent/home')