from pydantic import BaseModel, EmailStr


class Employee(BaseModel):
    # id: int
    name: str
    email: EmailStr
    password: str
    is_active: bool
    salary: float

    class Config:
        orm_mode = True


class EmployeeDepartment(BaseModel):
    # id: int
    dept_name: str
    employee_id: int

    class Config:
        orm_mode = True


