from sqlalchemy.orm import Session
from ..db.models import User


class UserCrud:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def read_all(self):
        return self.db.query(User).all()





