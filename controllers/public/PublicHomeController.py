from ..BaseController import *
from models.Person import *
from ..SignUpController import *

class PublicHome(BaseHandler):
    def get(self):
        print "running home get"
        user = users.get_current_user()
        if user:
            print user.user_id()
            query = Person.query()
            query.filter(Person.user_id == user.user_id())
            person = query.fetch(1)
            print person
            # Person exists, check role and send them to the right page
            try:
                role = person.role
                self.goHome(role)
                    
            except AttributeError:
                print "User has no role, man..."
                self.route('/templates/public/publicHome.html', True)

        else:
            print 'no user logged in, redirecting to main public page'
            self.route('/templates/public/publicHome.html', True)







