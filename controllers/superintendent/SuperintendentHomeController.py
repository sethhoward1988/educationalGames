from ..BaseController import *

class SuperintendentHome(BaseHandler):
    def get(self):
        user = users.get_current_user()
        templateOptions = {}
        templateOptions["nickname"] = user.nickname()
        templateOptions["district"] = {}

        school_district = self.app.config.get("webapp2_extras.sessions")["school_district"]

        templateOptions["district"]["name"] = school_district.name
        templateOptions["district"]["administrators"] = []

        for key in school_district.administrator:
            administrator = key.get()
            templateOptions["district"]["administrators"].append(administrator)

        schools = School.query(ancestor=school_district.key)
        schools = schools.fetch()
        templateOptions["district"]["schools"] = []

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

            templateOptions["district"]["schools"].append(currentSchool)

        template = JINJA_ENVIRONMENT.get_template('/templates/superintendent/superintendentHome.html')
        self.response.write(template.render(templateOptions))
