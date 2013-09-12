from ..BaseController import *
import educational-games.models

class PublicHome(BaseHandler):
    def get(self):
        user = users.get_current_user()
        print user
        
        if user:
            person_key = ndb.Key("Profile", user)
            person = Person.query_user(person_key)
            print person
            if person:
                # Person exists, check role and send them to the right page
                role = person.role
                if role == 'administrator':
                    print "User is an administrator"
                elif role == 'teacher':
                    print "User is a teacher"
                elif role == 'student':
                    print "User is a student"
                else:
                    print "User has no role, man..."

            else:
                # We need to create a profile for this new user, should be first time they've logged in
                print 'creating new person'
                person = Person(profile=user)
                person.put()
                self.route('/templates/signup.html')
        else:
            print 'no user logged in, redirecting to main public page'
            self.route('/templates/public/publicHome.html', True)

            