from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timedelta

class Syllabus(BaseModel):
    chapterName: str
    chapterVideo: str

class AddCourse(BaseModel):
    courseTitle: str
    createdDate: Optional[datetime]
    creator: str
    courseId: Optional[int]
    courseDesc: str
    courseCategory: str
    courseImage: str
    syllabus: List[Syllabus]

class LoginAccount(BaseModel):
    username: str
    password: str

class RegisterAccount(BaseModel):
    username: str
    password: str
    email: str

class Settings(BaseModel):
    authjwt_secret_key: str = "secret"
    authjwt_access_token_expires: timedelta = timedelta(hours=3)