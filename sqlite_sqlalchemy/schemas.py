from pydantic import BaseModel, EmailStr


class Employee(BaseModel):
    # id: int
    name: str
    email: EmailStr
    password: str
    is_active: bool
    salary: float
    dept_id: int

    class Config:
        orm_mode = True


class Department(BaseModel):
    # id: int
    dept_name: str

    class Config:
        orm_mode = True


