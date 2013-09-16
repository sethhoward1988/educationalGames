from ..BaseController import *

class SuperintendentEditDistrict(BaseHandler):
    def get(self):
        district = self.app.config.get("webapp2_extras.sessions")["school_district"].key.get()
        templateOptions = {
            'nickname': users.get_current_user().nickname(),
            'district': district,
            'administrators': []
        }
        for key in district.administrator:
            superintendent = key.get()
            templateOptions['administrators'].append(superintendent)

        template = JINJA_ENVIRONMENT.get_template('/templates/superintendent/superintendentEditDistrict.html')
        self.response.write(template.render(templateOptions))

    def post(self):
        district = self.app.config.get("webapp2_extras.sessions")["school_district"].key.get()
        try:
            name = self.request.get('name')
            if name == "":
                raise Exception("You must supply a school name")

            district.name = name
            district.put()
            self.redirect('/superintendent/district')

        except Exception, e:
            user = users.get_current_user()
            template = JINJA_ENVIRONMENT.get_template('/templates/superintendent/superintendentAddSchool.html')
            self.response.write(template.render({
                "nickname": user.nickname(),
                "district": district,
                "error": e
            }))
