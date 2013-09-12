from google.appengine.ext import ndb

class Person(ndb.Model):
    role = ndb.StringProperty(repeated=True)
    profile = ndb.UserProperty()
    f_name = ndb.StringProperty()
    l_name = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def query_user(cls, person_key):
        return cls.query(person_key)

class Class(ndb.Model):
	teacher = ndb.StructuredProperty(Person)
	students = ndb.StructuredProperty(Person, repeated=True)
	room_number = ndb.StringProperty()

class School(ndb.Model):
	administrator = ndb.StructuredProperty(Person, repeated=True)
	name = ndb.StringProperty()
	classes = ndb.StructuredProperty(Class, repeated=True)

class School_District(ndb.Model):
	administrator = ndb.StructuredProperty(Person, repeated=True)
	name = ndb.StringProperty()
	schools = ndb.StructuredProperty(School, repeated=True)