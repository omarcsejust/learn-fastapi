from sqlite_sqlalchemy.database import engine
from sqlite_sqlalchemy.models import Base


def generate_migration():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    generate_migration()

