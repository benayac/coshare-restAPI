import pymongo
import dns
import json

class Database():
    def __init__(self, URI):
        client = pymongo.MongoClient(URI)
        self.COURSES = client.courshare.COURSES
        self.USERS = client.courshare.USERS

    def insert_one_user(self, data):
        try:
            self.USERS.insert_one(data)
            return "Operation Success"
        except Exception as e:
            return str(e)

    def find_user_data(self, data):
        try:
            one_data = self.USERS.find_one({"username":data})
            if(one_data is None):
                return None
            else:
                return one_data
        except:
            return None

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

    def get_courses_from_type(self, type):
        try:
            return self.COURSES.find({"courseCategory": type})
        except Exception as e:
            return str(e)