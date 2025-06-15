from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional


class Student(BaseModel):
    name : str = 'Imran Hasan'
    age: Optional[int] = None
    subjects: List[str] = ['Math', 'Science', 'English']
    email: EmailStr
    cgpa: float = Field(gt=0.0, lt=4.0, default=0.0, description='Cumilative grade point average')


new_student = Student(name='Rekah Moni', age=26, email='abc@def.com', cgpa=2.5)

print(new_student)
print(type(new_student))
print(new_student.name)

new_student_dict = dict(new_student)
print(type(new_student_dict))

new_student_json = new_student.model_dump_json()
print(type(new_student_json))