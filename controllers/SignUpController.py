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

        query = Person().query()
        query.filter(Person.guid == guid)
        person = query.fetch(1)
        person = person[0]

        # try:
        if person.validated:
            print "This account has already been validated"
            self.goHome(person.role)
        else:
            print "Person is not validated..."
            person.validated = True
            person.put()
            template_values = {
                "guid": person.guid,
                "role": person.role
            }
            template = JINJA_ENVIRONMENT.get_template("/templates/signup.html")
            self.response.write(template.render(template_values))
        # except:
        #     template = JINJA_ENVIRONMENT.get_template("/templates/public/publicHome.html")
        #     self.response.write(template.render())

    def post(self, guid):
        print "We're posting some data... for " + guid
        
        user = users.get_current_user()
        
        if not user:
            self.redirect(users.create_login_url(self.request.uri))
            return

        query = Person().query()
        query.filter(Person.guid == guid)
        person = query.fetch(1)
        person = person[0]

        try:
            person.f_name = self.request.get('f_name')
            person.l_name = self.request.get('l_name')
            person.profile = user
            self.goHome(person.role)
            person.put()
        except:
            self.goHome(person.role)

        self.goHome(person.role)

class SignupPost(BaseHandler):
    def post(self):
        print "We're creating a new user..."
        self.response.headers['Content-Type'] = 'application/json'   
        # Verifying authenticity of signup request
        user = users.get_current_user()

        if user:
            requested_role = self.request.get('role')
            requestee_role = self.getUserRole(user)
            
            if  requestee_role == 'superintendent' && requested_role != 'principal' or
                requestee_role == 'principal' && requested_role != 'teacher' or
                requestee_role == 'teacher' && requested_role  != 'student':
                json = {
                    'error': 'User does not have permissions to create that role'
                }
            else:
                guid = str(uuid4())
                email = self.request.get('email')
                f_name = self.request.get('f_name')
                l_name = self.request.get('l_name')
                
                person = Person(email=email, role=requested_role, guid=guid)
                person.put()

                mail.send_mail(sender="Educational Games Team <smiles.seth@gmail.com>",
                      to=f_name + " " + l_name + " <" + email + ">",
                      subject="Educational Games Account Creation",
                      body="""
                        Welcome """ + f_name + """ """ + l_name + """!

                        Your Educational Games account has been created! The first thing you
                        will need to do is follow the link below to verify your account and
                        add some additional details.

                        """ + self.request.uri + "/" + guid + """

                        Please let us know if you have any questions.

                        - The Educational Games Team
                        """)
                json = {
                    'success': 'Account has been created'
                }
        else:
            json = {
                'error': 'No user logged in'
            }
        
        self.response.out.write(json.dumps(obj))


# $.ajax({
#     url:'/signup',
#     type:'POST',
#     data:{email:'smiles.seth@gmail.com',role:'superadmin', f_name:'Chloe', l_name:'Howard'},
#     success: function(data){ console.log(data)}
# })


