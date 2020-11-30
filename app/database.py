import pymongo
import dns
import json

class Database():
    def __init__(self, URI):
        client = pymongo.MongoClient(URI)
        self.COURSES = client.courshare.COURSES

    def get_all_courses(self):
        try:
            return self.COURSES.find({})
        except Exception as e:
            return str(e)

    def insert_one_course(self, data):
        try:
            self.COURSES.insert_one(data)
            return "Operation Success"
        except Exception as e:
            return str(e)

    def get_course_from_id(self, id):
        try:
            return self.COURSES.find_one({"courseId":id})
        except Exception as e:
            return str(e)