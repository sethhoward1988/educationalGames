from ..BaseController import *

class SuperintendentEditSchool(BaseHandler):
    def get(self, guid):
        schools = School.query(School.guid == guid).fetch(1)
        templateOptions = {
            'nickname': users.get_current_user().nickname(),
            'schools': []
        }
        for school in schools:
            currentSchool = {}
            currentSchool["name"] = school.name
            currentSchool["guid"] = school.guid
            currentSchool["principals"] = []
            currentSchool["principalLength"] = 0

            for key in school.administrator:
                principal = key.get()
                currentSchool["principals"].append(principal)
                currentSchool["principalLength"] += 1

            templateOptions["schools"].append(currentSchool)

        template = JINJA_ENVIRONMENT.get_template('/templates/superintendent/superintendentEditSchool.html')
        self.response.write(template.render(templateOptions))

    def post(self, guid):
        school = School.query(School.guid == guid).fetch(1)[0]
        school.name = self.request.get('name')
        school.put()
        self.redirect('/superintendent/home')