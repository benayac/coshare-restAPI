from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

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
