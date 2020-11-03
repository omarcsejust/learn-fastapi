from pydantic import BaseModel, EmailStr


class User(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    address: str
    city: str
    state: str
    country: str
    


