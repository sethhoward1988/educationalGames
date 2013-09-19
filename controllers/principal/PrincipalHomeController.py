from ..BaseController import *

class PrincipalHome(BaseHandler):
    def get(self):
        user = users.get_current_user()
        templateOptions = {}
        templateOptions["nickname"] = user.nickname()
        templateOptions["classRooms"] = []

        school = self.app.config.get("webapp2_extras.sessions")["school"]

        templateOptions["school"] = school
        classRooms = Class.query(ancestor=school.key).fetch()

        for klass in classRooms:
            currentKlass = {}
            currentKlass["room_number"] = klass.room_number
            currentKlass["teachers"] = []

            for key in klass.teacher:
                currentKlass["teachers"].append(key.get())

        print templateOptions
        template = JINJA_ENVIRONMENT.get_template('/templates/principal/principalHome.html')
        self.response.write(template.render(templateOptions))