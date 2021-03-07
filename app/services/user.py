from sqlalchemy.orm import Session
from ..schemas import User as UserSchema
from ..db.models import User
from ..cruds.user_crud import UserCrud


class UserService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def add_user(self, user_schema=UserSchema, image: bytes = None):
        db_user_crud = UserCrud(db=self.db)
        user = User(name=user_schema.name, image=image)
        return db_user_crud.create(user=user)





