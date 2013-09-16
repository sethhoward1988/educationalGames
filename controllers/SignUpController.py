from BaseController import *
from google.appengine.api import mail
from models.Person import *
from uuid import uuid4

class Signup(BaseHandler):
    def get(self, guid):
        print "We've hit the signup page for " + guid
        user = users.get_current_user()
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return

        query = Person.query(Person.guid == guid)
        person = query.fetch(1)
        person = person[0]

        if person.email != user.email():
            template_values = {
                'message': "<p>You're attempting to setup a user that has a different account than the one that is logged in! Please logout of your current account and try to setup your account again."
            }
            template = JINJA_ENVIRONMENT.get_template("/templates/error.html")
            self.response.write(template.render(template_values))
            return
        try:
            if person.validated:
                print "This account has already been validated"
                self.goHome(person.role[0])
            else:
                print "Person is not validated..."
                template_values = {
                    "guid": person.guid,
                    "role": person.role[0]
                }
                template = JINJA_ENVIRONMENT.get_template("/templates/signup.html")
                self.response.write(template.render(template_values))
        except:
            template = JINJA_ENVIRONMENT.get_template("/templates/public/publicHome.html")
            self.response.write(template.render())

    def post(self, guid):
        print "We're posting some data... for " + guid
        
        user = users.get_current_user()
        
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return

        query = Person.query(Person.guid == guid)
        person = query.fetch(1)
        person = person[0]

        try:
            person.f_name = self.request.get('f_name')
            person.l_name = self.request.get('l_name')
            person.profile = user
            person.validated = True
            person.user_id = user.user_id()
            self.goHome(person.role[0])
            person.put()
        except:
            self.goHome(person.role[0])

        self.goHome(person.role[0])

class UserCreation(BaseHandler):
    def createUser(self, user_info, user, uri):
        # Verifying authenticity of signup request
        if user:
            print "Printing User Info Object"
            print user_info
            requested_role = user_info["role"]
            if users.is_current_user_admin():
                requestee_role = 'admin'
            else:
                requestee_role = self.getCurrentUserRole(user)[0]
            
            print requestee_role
            print requested_role
            
            if requestee_role == 'superintendent' and requested_role not in ['principal','teacher','student']:
                return {
                    'error': 'User does not have permissions to create that role'
                }
            elif requestee_role == 'principal' and requested_role not in ['teacher', 'student']:
                return {
                    'error': 'User does not have permissions to create that role'
                }
            elif requestee_role == 'teacher' and requested_role  not in ['student']:
                return {
                    'error': 'User does not have permissions to create that role'
                }
            elif requestee_role == False:
                return {
                    'error': 'User does not have permissions to create that role'
                }
            else:
                # Check to see if user already exists
                try:    
                    email = user_info.email
                    query = Person.query(Person.email == email)
                    person = query.fetch(1)
                    person = person[0]
                    print person
                    if person:
                        print "User already exists..."
                        return {
                            'error': 'User already exists'
                        }

                except:
                    print "Creating User..."
                    guid = str(uuid4())
                    f_name = user_info["f_name"]
                    l_name = user_info["l_name"]
                    
                    person = Person(f_name=f_name, l_name=l_name, email=user_info["email"], role=[user_info["role"]], guid=guid)
                    person.put()
                    # self.sendEmail(f_name, l_name, user_info["email"], guid, uri)
                    return person
        else:
            return {
                'error': 'No user logged in'
            }

    def sendEmail(self, f_name, l_name, email, guid, uri):
        mail.send_mail(sender="Educational Games Team <smiles.seth@gmail.com>",
              to=f_name + " " + l_name + " <" + email + ">",
              subject="Educational Games Account Creation",
              body="""
                Welcome """ + f_name + """ """ + l_name + """!

                Your Educational Games account has been created! The first thing you
                will need to do is follow the link below to verify your account and
                add some additional details.

                """ + uri + "/" + guid + """

                Please let us know if you have any questions.

                - The Educational Games Team
                """)


# $.ajax({
#     url:'/signup',
#     type:'POST',
#     data:{email:'smiles.seth@gmail.com',role:'superadmin', f_name:'Chloe', l_name:'Howard'},
#     success: function(data){ console.log(data)}
# })


