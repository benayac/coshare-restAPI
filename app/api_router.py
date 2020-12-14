from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from database import Database
from models import *
from helper import *
from datetime import datetime

URI = "mongodb+srv://admin:admin@cluster0.nx34d.mongodb.net/<dbname>?retryWrites=true&w=majority"
router = APIRouter()
db = Database(URI)

@router.post("/register")
def register(account: RegisterAccount):
    try:
        return request_success(db.insert_one_user(account.dict()))
    except Exception as e:
        return request_error(e)

@router.post("/login")
def login(account: LoginAccount, Authorize: AuthJWT = Depends()):
    try:
        account.username = account.username.lower()
        entity = db.find_user_data(account.username)
        if(entity is None):
            return request_success("Could not find user")
        if(entity["password"] != account.password):
            return request_success("Could not find user")
        access_token = Authorize.create_access_token(account.username)
        return request_success({"message":"Login successful", "access_token":access_token})
    except Exception as e:
        return request_error(e)

@router.get("/get_courses")
def get_courses(type: int):
    try:
        data = []
        if(type == 0):
            data = db.get_all_courses()
        elif(type == 1):
            data = db.get_courses_from_type("Programming")
        elif(type == 2):
            data = db.get_courses_from_type("Data Science")
        elif(type == 3):
            data = db.get_courses_from_type("UX Design")
        elif(type == 4):
            data = db.get_courses_from_type("Web Development")
        elif(type == 5):
            data = db.get_courses_from_type("Marketing")
        return request_success(serialize_data(data))
    except Exception as e:
        return request_error(e)

@router.post("/post_course")
def post_course(course: AddCourse, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        id = db.get_all_courses().count()
        course.courseId = id+1
        course.createdDate = datetime.now()
        new_syllabus = []
        for syl in course.syllabus:
            syl.chapterVideo = youtube_to_id(syl.chapterVideo)
            new_syllabus.append(syl)
        course.syllabus = new_syllabus
        return request_success(db.insert_one_course(course.dict()))
    except Exception as e:
        return request_error(e)

@router.get("/course")
def get_course(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        data = db.get_course_from_id(id)
        return request_success(serialize_data(data))
    except Exception as e:
        return request_error(e)