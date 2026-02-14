from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings


SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{settings.db_user}:{settings.db_password}@localhost:{settings.db_port}/{settings.db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


