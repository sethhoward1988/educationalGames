from google.appengine.ext import ndb

# class Game(ndb.Model):


class Score(ndb.Model):
    gameName = ndb.StringProperty()
    email = ndb.StringProperty()
    correct = ndb.FloatProperty()
    peeked = ndb.FloatProperty()
    skipped = ndb.FloatProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)