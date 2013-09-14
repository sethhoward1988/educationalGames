import os
import urllib
import json

from google.appengine.api import users
from google.appengine.ext import ndb
from webapp2_extras import sessions
from models.Person import *

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(os.path.dirname(__file__))),
    extensions=['jinja2.ext.autoescape'])

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

    def route(self, template, public=False):
        user = users.get_current_user()
        template_values = self.getTemplateValues(user).items() + self.getBaseTemplateValues(user).items()
        if public:
            template = JINJA_ENVIRONMENT.get_template(template)
            self.response.write(template.render(template_values))
        else:
            if user:
                # if not self.session.get('user_role'):
                template = JINJA_ENVIRONMENT.get_template(template)
                self.response.write(template.render(template_values))
            else:
                self.redirect(users.create_login_url(self.request.uri))
    
    def goHome(self, role):
        self.redirect("/" + role)

    def getTemplateValues(self, user):
        return {}

    def getBaseTemplateValues(self, user):
        nickname = ''
        if user:
            nickname = user.nickname()
        return {
                'nickname': nickname
            }

    def getCurrentUserRole(self, user):
        try:
            print "getting current user"
            query = Person.query(Person.user_id == user.user_id())
            person = query.fetch(1)
            person = person[0]
            return person.role
        except:
            return False

    def getCurrentPerson():
        user = users.get_current_user()
        try:
            print "getting current user"
            query = Person.query(Person.user_id == user.user_id())
            person = query.fetch(1)
            person = person[0]
            return person.role
        except:
            return False

    def baseRedirect(self):
        user = users.get_current_user()
        role = self.getCurrentUserRole(user)
        try:
            self.goHome(role[0])
        except:
            self.route("/templates/public/publicHome.html", True)





        