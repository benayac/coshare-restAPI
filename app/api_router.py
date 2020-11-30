from fastapi import APIRouter
from database import Database
from models import *
from helper import *
from datetime import datetime

URI = "mongodb+srv://admin:admin@cluster0.nx34d.mongodb.net/<dbname>?retryWrites=true&w=majority"
router = APIRouter()
db = Database(URI)

@router.get("/get_courses")
def get_courses():
    try:
        courses = db.get_all_courses()
        response = collection_to_list(courses)
        return request_success(response)
    except Exception as e:
        return request_failed(str(e))

@router.post("/post_course")
def post_course(course: AddCourse):
    try:
        id = db.get_all_courses().count()
        course.courseId = id+1
        course.createdDate = datetime.now()
        return request_success(db.insert_one_course(course.dict()))
    except Exception as e:
        return request_failed(str(e))

@router.get("/course")
def get_course(id: int):
    try:
        data = db.get_course_from_id(id)
        return request_success(serialize_data(data))
    except Exception as e:
        return request_failed(str(e))