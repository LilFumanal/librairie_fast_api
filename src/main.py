from fastapi import FastAPI
from sqlalchemy.orm import session
from config import connexion
from router import ouvrage_router

connexion.Base.metadata.create_all(connexion.engine)
app = FastAPI()
app.include_router(ouvrage_router.app)
# Dependency
def get_db():
  db = connexion.SessionLocal()
  try:
    yield db
  finally:
    db.close()