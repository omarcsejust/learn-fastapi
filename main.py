from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from basic_crud.user_dao import get_user_data, get_user_by_id, add_user
from basic_crud.models import User
from sqlite_sqlalchemy import models, schemas, crud
from sqlite_sqlalchemy.database import engine, SessionLocal
import uvicorn

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


# offset & limit are passed as Query Parameter, (we can use also Path Parameter)
@app.get('/get-employees')
def get_all_employees(offset: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return crud.get_employees(db=db, skip=offset, limit=limit)


@app.post('/add-employee-department')
def add_employee_department(employee_department: schemas.Department, db: Session = Depends(get_db)):
    return crud.create_department(db=db, employee_department=employee_department)


@app.get('/get-employee-department')
def get_emp_dept(db: Session = Depends(get_db)):
    return crud.get_employee_with_dept(db=db)


@app.get('/test-keycloak')
def test_keycloak():
    from keycloak import KeycloakOpenID

    # Configure client
    # keycloak_openid = KeycloakOpenID(server_url="http://127.0.0.1:8080/auth/",
    #                                  client_id="master-realm",
    #                                  realm_name="master",
    #                                  client_secret_key="c5c25fef-b247-4876-8f8e-c8b90780daee")
    # # Get WellKnow
    # config_well_know = keycloak_openid.well_know()
    #
    # # Get Token
    # token = keycloak_openid.token("omar", "omar19")
    # # token = keycloak_openid.token("user", "password", totp="012345")
    # return token
    #
    # # Get Userinfo
    # userinfo = keycloak_openid.userinfo(token['access_token'])
    # return userinfo

    from keycloak import KeycloakAdmin

    # connect to keycloak server
    admin = KeycloakAdmin(server_url='http://127.0.0.1:8080/auth/',
                          username='admin',
                          password='admin123',
                          realm_name='master',
                          verify=True)

    user_groups = admin.get_user_groups(user_id="9018d0fe-4dc6-41bf-ad9f-02fd5fe3cd1a")
    # return user_groups

    # Add user
    # new_user = admin.create_user({"email": "example@example.com",
    #                                        "username": "example@example.com",
    #                                        "enabled": True,
    #                                        "firstName": "Example",
    #                                        "lastName": "Example"})
    # return new_user

    # Get User
    user = admin.get_user("58b704de-f5e6-422b-aa59-bf36a45d62f5")
    return user


@app.post('/verify-email')
def test_keycloak(token: str):
    import jwt
    decoded_data = jwt.decode(token, algorithms=['HS256'], verify=False)
    return decoded_data['eml']

@app.get("/test-fb-page-chat")
def test_fb_page_chat():
    import facebook

    # at = "EAAFpKBaP7yABAM0rtk6VAZCtRuIECOOipxlGPPMVe8A5tDlgbZCagzNn4Xv0H7LKMjKWoVtM6gCnGLOIjtfBmwe80VgXc9LvIyZC4ZCnBo1c2lzMpO6wljCeJD3f6lCaCWtZB2ubGZAYVhd2oNONthhqVNXlioQr7aNCbH9ZBsvdAZDZD"
    # at = "EAAFpKBaP7yABAJMRkjF7TvSKz5rZCOZCgPC72zfjHFLzo9DvowJRpXvdy3HBZAcZAUHxmiRaFlZAmh12ftzwAQTMP6BLyux3iVZBL1Fmb2Kmc4E115lTXa19Y6RDEipRXpMndDGd6asVTiPnzH7B1BE9dr2zlscdAQGuEQdwj3UJKtj3oR7ZAzYZCkEqi79MJS0ZD"
    at = "EAAFpKBaP7yABABkBWqrKnUyAkeQEFqG2lKaKG1SZBeUqZAIPNoluStl8uMQZBHc9tSEjF5CxAEAgyyuzzKf09pirBnSkMBufrblOZCXBRVZAYdwosShDXpyOg30yinGKSpkMTv3jUwPgt9jqBhzZASJ8bkhuw1CZBMZAuVMCwLjWMAZDZD"
    at = "EAADfZC0grTZAgBALGZBJl30tY4onRXGm0QYD2ZCjADbUXp9QUMswZCW1ZCARo1FvIfPb3l5EOuI21rJ387F0vFMRlirazECi5oFmkLiJtOWkXH56Ge0OB8tUpQdjoMRFK3FJZB4GUxefd8N88LvcdblpI3fsdIHCj7Ot6V5tKNQsZCZBeU6x0v7KKLR2xu0y1LOkZD"
    pid = "102343285156064"
    api = facebook.GraphAPI(at)
    args = {'fields': 'message,from'}  # requested fields
    conv = api.get_object('me/conversations')
    msg = api.get_object(conv['data'][0]['id'] + '/messages')
    # return msg
    for el in msg['data']:
        content = api.get_object(el['id'], **args)  # adding the field request
        print(content)


@app.get("/test-fb-page-chat/py-requests")
def test_fb_page_chat_py_requests():
    import requests
    page_access_token = "EAADfZC0grTZAgBAHYkTZCPFNiZAWqLlLtjFW2vnhtzjtwKTz68YWZBv2AbsKCs7mb3e9qKubPYx1JNVHgEjHfkaxsGcWGy3kJJc0cZBDTBPIRcvLUD44lqdtsDqZA9FerZApR3Pf9ethtWMqZBcoEMkcAxmtZBBAAP8LC5JwuwQe0ElMpErLMsfVuY52b4c1J3tPDm7oYSbfZBGOUzXq0UOUEii"
    uri = "https://graph.facebook.com/v9.0/me/conversations?fields=messages{message,from},unread_count&access_token=" + page_access_token
    data = requests.get(uri)
    return data.json()


@app.get("/get-fb-user-account-info")
def get_fb_user_account_info():
    import requests
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", debug=True, reload=True)
