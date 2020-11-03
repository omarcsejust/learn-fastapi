from sqlalchemy.orm import Session
from sqlite_sqlalchemy import models, schemas

# CRUD for Employee


def create_employee(employee: schemas.Employee, db: Session):
    db_employee = models.Employee(name=employee.name, email=employee.email, password=employee.password,
                                  salary=employee.salary)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_employee(db: Session, employee_id: int):
    return db.query(models.Employee).filter(models.Employee.id == employee_id).first()


def get_employee_by_email(db: Session, employee_email: str):
    return db.query(models.Employee).filter(models.Employee.email == employee_email).first()


def get_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()


def delete_employee(db: Session, employee_id: int):
    affected_rows = db.query(models.Employee).filter(models.Employee.id == employee_id).delete()
    db.commit()
    return affected_rows


