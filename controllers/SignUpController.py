from BaseController import *
from google.appengine.api import mail
from models.Person import *
from uuid import uuid4

class Signup(BaseHandler):
    def get(self, user_id):
        print "We've hit the signup page for " + user_id

        query = Person().query()
        query.filter(Person.user_id == user_id)
        person = query.fetch(1)

        try:
            if person.validated:
                print "This account has already been validated"
                self.goHome(person.role)
            else:
                person.validated = True
                person.put()
                user = users.get_current_user()
                template_values = {
                    user_id: person.user_id,
                    role: person.role
                }
                template = JINJA_ENVIRONMENT.get_template(template)
                self.response.write(template.render(template_values))
        except:
            template = JINJA_ENVIRONMENT.get_template("/templates/public/publicHome.html")
            self.response.write(template.render())

    def post(self, user_id):
        query = Person().query()
        query.filter(Person.user_id == user_id)
        person = query.fetch(1)

        try:
            person.f_name = self.request.get('f_name')
            person.l_name = self.request.get('l_name')
            person.put()
        except:
            self.goHome(person.role)

class SignupPost(BaseHandler):
    def post(self):
        # Need to verify authenticity of this request
        guid = str(uuid4())
        email = self.request.get('email')
        f_name = self.request.get('f_name')
        l_name = self.request.get('l_name')
        role = self.request.get('role')
        person = Person(email=email, role=role, guid=guid)
        person.put()

        mail.send_mail(sender="Educational Games Team <smiles.seth@gmail.com>",
              to=f_name + " " + l_name + " <" + email + ">",
              subject="Educational Games Account Creation",
              body="""
                Welcome """ + f_name + """ """ + l_name + """!

                Your Educational Games account has been created! The first thing you
                will need to do is follow the link below to verify your account and
                add some additional details.

                """ + self.request.uri + guid + """

                Please let us know if you have any questions.

                - The Educational Games Team
                """)
        self.response.headers['Content-Type'] = 'application/json'   
        obj = {
            'success': 'Account created'
        } 
        self.response.out.write(json.dumps(obj))


# $.ajax({
#     url:'/signup',
#     type:'POST',
#     data:{email:'smiles.seth@gmail.com',role:'superadmin', f_name:'Chloe', l_name:'Howard'},
#     success: function(data){ console.log(data)}
# })


