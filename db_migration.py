from app.db import models
from app.db.database import engine


def migrate_db():
    models.Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    migrate_db()


