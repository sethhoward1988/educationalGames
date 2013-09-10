import logging
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb
from webapp2_extras import sessions

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

class User(ndb.Model):
    role = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_user(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key)

class BaseHandler(webapp2.RequestHandler):              # taken from the webapp2 extrta session example
    def dispatch(self):                                 # override dispatch
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)       # dispatch the main handler
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

    def route(self, template):
        user = users.get_current_user()
        if user:
            print self.session.get('user_role')
            if not self.session.get('user_role'):
                print "Creating new role..."
                ancestor_key = ndb.Key("User", user.email())
                userObject = User.query_user(ancestor_key).fetch()

                if len(userObject) > 0:
                    print "found existing role..."
                    self.session['user_role'] = userObject[0].role
                else:
                    newUser = User(parent=ndb.Key("User", user.email()), role='basic')
                    newUser.put()
                    self.session['user_role'] = 'basic'        

            template_values = self.getTemplateValues(user).items() + self.getBaseTemplateValues(user).items()
            print self.session.get('user_role')
            template = JINJA_ENVIRONMENT.get_template(template)
            self.response.write(template.render(template_values))
        else:
            self.redirect(users.create_login_url(self.request.uri))

    def getTemplateValues(self, user):
        return {}

    def getBaseTemplateValues(self, user):
        return {
                'nickname': user.nickname(),
                'logout_url': '/logout'
            }
        

class Logout(BaseHandler):
    def get(self):
        user = users.get_current_user()
        self.session.clear()
        self.redirect(users.create_logout_url('/'))

class MainPage(BaseHandler):
    def get(self):
        self.route('/templates/index.html')

class GeoPage(BaseHandler):
    def get(self):
        self.route('/templates/geo.html')

class SpellingPage(BaseHandler):
    def get(self):
        self.route('/templates/spelling.html')

class MathPage(BaseHandler):
    def get(self):
        self.route('/templates/math.html')

class Account(BaseHandler):
    def get(self):
        self.route('/templates/account.html')

    def getTemplateValues(self, user):
        return { 
            'role': self.session['user_role'],
            'nickname': user.nickname(),
            'email': user.email()
        }

class Results(BaseHandler):
    def get(self):
        self.route('/templates/results.html')

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'some-secret-key',
}

app = webapp2.WSGIApplication([
    (r'/', MainPage),
    (r'/geo', GeoPage),
    (r'/spelling', SpellingPage),
    (r'/math', MathPage),
    (r'/results', Results),
    (r'/account', Account),
    (r'/logout', Logout)
], debug=True, config = config)

