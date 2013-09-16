from ..BaseController import *
from ..SignUpController import *
from uuid import uuid4
import re

class SuperintendentAddSchool(BaseHandler):
    def get(self):
        self.route('/templates/superintendent/superintendentAddSchool.html')
        
    def post(self):
        try:
            postType = self.request.get("type")
            school_name = self.request.get("name")
            email = self.request.get("email")
            school_guid = self.request.get('school_guid')

            if postType == "delete":
                self.delete(school_guid)

            elif postType == "newAdmin":
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    raise Exception("Email is not valid") 
                self.newAdmin(email, school_guid)

            elif postType == "update":
                if school_name == "":
                    raise Exception("You must supply a school name")
                self.update(school_guid, school_name)

            elif postType == "new":
                if school_name == "":
                    raise Exception("You must supply a school name")
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    raise Exception("Email is not valid") 
                self.new(email, school_name)

            self.redirect('/superintendent/home')
                
        except Exception, e:
            user = users.get_current_user()
            template = JINJA_ENVIRONMENT.get_template('/templates/superintendent/superintendentAddSchool.html')
            self.response.write(template.render({
                "nickname": user.nickname(),
                "error": e
            }))

    def new(self, email, school_name):
        principal = self.getNewOrExistingPerson(email)
        principal.role = ['principal']
        new_school = School(parent=self.app.config.get("webapp2_extras.sessions")["school_district"].key, administrator=[principal.key], guid=str(uuid4()), name=school_name)
        new_school.put()

    def update(self, guid, school_name):
        school = self.getExistingSchool(guid)
        school.name = school_name
        school.put()

    def newAdmin(self, email, guid):
        principal = self.getNewOrExistingPerson(email)
        school = self.getExistingSchool(guid)
        administrator_keys = []
        for key in school.administrator:
            administrator_keys.append(key)

        administrator_keys.append(principal.key)
        school.administrator = administrator_keys
        school.put()

    def delete(self, guid):
        school = self.getExistingSchool(guid)
        school.key.delete()



    # Util Methods

    def getExistingSchool(self, guid):
        return School.query(School.guid == guid).fetch(1)[0]

    def getNewOrExistingPerson(self, email):
        query = Person.query(Person.email == email)
        principal = query.fetch()
        if len(principal) > 0:
            # Person Already exists...
            principal = principal[0]
            return principal
        else:
            # We are creating an entirely new user
            createUser = UserCreation(BaseHandler)# Create a new person...
            principal = createUser.createUser({
                "f_name": '',
                "l_name": '',
                "email": self.request.get("email"),
                "role": "principal"
            }, users.get_current_user(), self.request.uri)
            return principal



