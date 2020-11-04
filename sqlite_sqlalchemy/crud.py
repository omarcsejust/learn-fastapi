from sqlalchemy.orm import Session
from sqlite_sqlalchemy import models, schemas

# CRUD for Employee


# add employee to employees table
def create_employee(employee: schemas.Employee, db: Session):
    db_employee = models.Employee(name=employee.name, email=employee.email, password=employee.password,
                                  salary=employee.salary, dept_id=employee.dept_id)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


# get employee by id
def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


# get employee by email
def get_employee_by_email(db: Session, employee_email: str):
    return db.query(models.Employee).filter(models.Employee.email == employee_email).first()


# get all employees by offset and limit
def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee)\
        .offset(skip)\
        .limit(limit)\
        .all()


# delete employee by id
def delete_employee(db: Session, employee_id: int):
    affected_rows = db.query(models.Employee).filter(models.Employee.id == employee_id).delete()
    db.commit()
    return affected_rows


# CRUD for EmployeeDepartment


# create EmployeeDepartment record
def create_department(db: Session, employee_department: schemas.Department):
    db_department = models.Department(dept_name=employee_department.dept_name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department


# joining two tables(employees & employee_departments)
def get_employee_with_dept(db: Session):
    return db.query(models.Employee, models.Department).\
        join(models.Department).all()
    # return db.query(models.Employee.name, models.Employee.salary, models.Department.dept_name).\
    #  join(models.Department).all()





