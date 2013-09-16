from BaseController import *
from uuid import uuid4
from google.appengine.api import users
from google.appengine.api import *

class Populate(BaseHandler):
    def get(self):

        superintendent = Person(role=["superintendent"], email="superintendent@example.com", guid=str(uuid4()))
        superintendent.put()

        principal1 = Person(role=["principal"],email="principal1@example.com", guid=str(uuid4()), f_name="Barry", l_name="Bonds")
        principal1.put()

        principal2 = Person(role=["principal"],email="principal2@example.com", guid=str(uuid4()), f_name="Alec", l_name="Baldwin")
        principal2.put()

        principal3 = Person(role=["principal"],email="principal3@example.com", guid=str(uuid4()), f_name="Steve", l_name="Wozniak")
        principal3.put()

        teacher1 = Person(role=["teacher"], email="teacher1@example.com", guid=str(uuid4()))
        teacher1.put()

        teacher2 = Person(role=["teacher"], email="teacher2@example.com", guid=str(uuid4()))
        teacher2.put()

        teacher3 = Person(role=["teacher"], email="teacher3@example.com", guid=str(uuid4()))
        teacher3.put()

        student1 = Person(role=["student"], email="student1@example.com", guid=str(uuid4()))
        student1.put()

        student2 = Person(role=["student"], email="student2@example.com", guid=str(uuid4()))
        student2.put()

        student3 = Person(role=["student"], email="student3@example.com", guid=str(uuid4()))
        student3.put()

        student4 = Person(role=["student"], email="student4@example.com", guid=str(uuid4()))
        student4.put()

        schoolDistrict = School_District(name="Nebo School District", administrator=[superintendent.key], guid=str(uuid4()))
        schoolDistrict.put()

        school1 = School(parent=schoolDistrict.key, administrator=[principal1.key], name="Orchard Hills", guid=str(uuid4()))
        school1.put()

        school2 = School(parent=schoolDistrict.key, administrator=[principal2.key], name="Leonard", guid=str(uuid4()))
        school2.put()

        school3 = School(parent=schoolDistrict.key, administrator=[principal3.key], name="Rolling Hills", guid=str(uuid4()))
        school3.put()

        classRoom = Class(parent=school1.key, room_number="R205", teacher=[teacher1.key], students=[student1.key, student2.key, student3.key, student4.key], guid=str(uuid4()))
        classRoom.put()

        

        

