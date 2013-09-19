from ..BaseController import *
from ..SignUpController import *
from uuid import uuid4
import re

class PrincipalAddClass(BaseHandler):
    def get(self):
        self.route('/templates/principal/principalAddClass.html')
        
    def post(self):
        try:
            postType = self.request.get("type")
            class_room = self.request.get("name")
            email = self.request.get("email")
            class_guid = self.request.get('class_guid')

            if postType == "delete":
                self.delete(class_guid)

            elif postType == "newTeacher":
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    raise Exception("Email is not valid") 
                self.newAdmin(email, class_guid)

            elif postType == "update":
                if room_number == "":
                    raise Exception("You must supply a school name")
                self.update(class_guid, class_room)

            elif postType == "new":
                if room_number == "":
                    raise Exception("You must supply a school name")
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    raise Exception("Email is not valid") 
                self.new(email, class_room)

            self.redirect('/principal/home')
                
        except Exception, e:
            user = users.get_current_user()
            template = JINJA_ENVIRONMENT.get_template('/templates/superintendent/superintendentAddSchool.html')
            self.response.write(template.render({
                "nickname": user.nickname(),
                "error": e
            }))

    def new(self, email, room_number):
        teacher = self.getNewOrExistingPerson(email)
        teacher.role = ['teacher']
        new_class = Class(parent=self.app.config.get("webapp2_extras.sessions")["school"].key, teacher=[teacher.key], guid=str(uuid4()), room_number=room_number)
        new_school.put()

    def update(self, guid, room_number):
        classRoom = self.getExistingClass(guid)
        classRoom.room_number = room_number
        school.put()

    def newAdmin(self, email, guid):
        teacher = self.getNewOrExistingPerson(email)
        classRoom = self.getExistingClass(guid)
        administrator_keys = []
        for key in school.administrator:
            administrator_keys.append(key)

        administrator_keys.append(teacher.key)
        classRoom.teacher = administrator_keys
        classRoom.put()

    def delete(self, guid):
        classRoom = self.getExistingClass(guid)
        classRoom.key.delete()



    # Util Methods

    def getExistingClass(self, guid):
        return Class.query(Class.guid == guid).fetch(1)[0]

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




