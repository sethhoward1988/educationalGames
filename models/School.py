from google.appengine.ext import ndb

class School_District(ndb.Model):
    administrator = ndb.KeyProperty(kind="Person", repeated=True)
    schools = ndb.KeyProperty(kind="School", repeated=True)
    name = ndb.StringProperty()

class School(ndb.Model):
    administrator = ndb.KeyProperty(kind="Person", repeated=True)
    classes = ndb.KeyProperty(kind="Class", repeated=True)
    name = ndb.StringProperty()

class Class(ndb.Model):
    teacher = ndb.KeyProperty(kind="Person", repeated=True)
    students = ndb.KeyProperty(kind="Person", repeated=True)
    room_number = ndb.StringProperty()