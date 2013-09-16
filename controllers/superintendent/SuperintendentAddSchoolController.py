from ..BaseController import *
from ..SignUpController import *
from uuid import uuid4

class SuperintendentAddSchool(BaseHandler):
    def get(self):
        self.route('/templates/superintendent/superintendentAddSchool.html')
        
    def post(self):
        query = Person.query(Person.email == self.request.get("email"))
        principal = query.fetch()
        if len(principal) > 0:
            # Person Already exists...
            if len(principal["role"]) > 0:
                # User already has a role...
                print "user does not have role..."
            else:
                print "User already exists and has a role of " + principal["role"]
        else:
            createUser = UserCreation(BaseHandler)# Create a new person...
            principal = createUser.createUser({
                "f_name": self.request.get("f_name"),
                "l_name": self.request.get("l_name"),
                "email": self.request.get("email"),
                "role": "principal"
                }, users.get_current_user(), self.request.uri)
            print principal
            
            new_school = School(parent=self.app.config.get("webapp2_extras.sessions")["school_district"].key, administrator=[principal.key], guid=str(uuid4()), name=self.request.get("name"))
            new_school.put()
            self.redirect('/superintendent/home')