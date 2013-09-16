from google.appengine.ext import ndb

class Person(ndb.Model):
    role = ndb.StringProperty(choices=['superadmin','superintendent','principal','teacher','student'], repeated=True)
    profile = ndb.UserProperty()
    user_id = ndb.StringProperty()
    f_name = ndb.StringProperty(default="No")
    l_name = ndb.StringProperty(default="Name")
    full_name = ndb.ComputedProperty(lambda self: self.f_name + " " + self.l_name)
    email = ndb.StringProperty()
    guid = ndb.StringProperty()
    validated = ndb.BooleanProperty(default=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class School_District(ndb.Model):
    administrator = ndb.KeyProperty(kind="Person", repeated=True)
    guid = ndb.StringProperty()
    name = ndb.StringProperty()

class School(ndb.Model):
    administrator = ndb.KeyProperty(kind="Person", repeated=True)
    guid = ndb.StringProperty()
    name = ndb.StringProperty()

class Class(ndb.Model):
    teacher = ndb.KeyProperty(kind="Person", repeated=True)
    students = ndb.KeyProperty(kind="Person", repeated=True)
    room_number = ndb.StringProperty()
    guid = ndb.StringProperty()