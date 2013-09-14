from google.appengine.ext import ndb

class Person(ndb.Model):
    role = ndb.StringProperty(choices=['superadmin','superintendent','principal','teacher','student'], repeated=True)
    profile = ndb.UserProperty()
    user_id = ndb.StringProperty()
    f_name = ndb.StringProperty()
    l_name = ndb.StringProperty()
    email = ndb.StringProperty()
    guid = ndb.StringProperty()
    validated = ndb.BooleanProperty(default=False)
    date = ndb.DateTimeProperty(auto_now_add=True)