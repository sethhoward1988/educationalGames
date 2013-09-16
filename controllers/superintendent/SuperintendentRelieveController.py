from ..BaseController import *

class SuperintendentRelieve(BaseHandler):
    def post(self):
        principal_guid = self.request.get('principal_guid')
        school_guid = self.request.get('school_guid')

        principal = Person.query(Person.guid == principal_guid).fetch(1)[0]
        new_role = []

        for role in principal.role:
            if(role != 'principal'):
                new_role.append(role)

        principal.role = new_role
        principal.put()

        school = School.query(School.guid == school_guid).fetch(1)[0]
        new_admin_keys = []

        for key in school.administrator:
            if(key.get().guid != principal_guid):
                new_admin_keys.append(key)

        school.administrator = new_admin_keys
        school.put()

        self.redirect('/superintendent/home')


