from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from basic_crud.user_dao import get_user_data, get_user_by_id, add_user
from basic_crud.models import User
from sqlite_sqlalchemy import models, schemas, crud
from sqlite_sqlalchemy.database import engine, SessionLocal

# migrate SQLite db
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get('/')
def get_users():
    return get_user_data(20)


@app.get('/user/{user_id}')
def get_user(user_id: int):
    return get_user_by_id(user_id)


@app.post('/add-user')
def add_user_data(user: User):
    add_user(user)


# CRUD using SQLAlchemy ORM

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post('/add-employee')
def add_employee(employee: schemas.Employee, db: Session = Depends(get_db)):
    return crud.create_employee(employee=employee, db=db)


@app.get('/get-employee/{employee_id}', response_model=schemas.Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee(db=db, employee_id=employee_id)
    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found!"
        )
    return employee


@app.delete('/delete-employee/{employee_id}')
def remove_employee(employee_id: int, db: Session = Depends(get_db)):
    affected_rows = crud.delete_employee(employee_id=employee_id, db=db)
    status_code = 200
    msg = "Deleted Successfully"
    if affected_rows == 0:
        status_code = 404
        msg = "Employee not found"

    raise HTTPException(
        status_code=status_code,
        detail=msg
    )


