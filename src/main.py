from fastapi import FastAPI
from sqlalchemy.orm import session
from config import connexion
from router import ouvrage_router, commentaire_router, client_router

connexion.Base.metadata.create_all(connexion.engine)
app = FastAPI()
app.include_router(ouvrage_router.app)
app.include_router(commentaire_router.app)
app.include_router(client_router.app)
# Dependency
def get_db():
  db = connexion.SessionLocal()
  try:
    yield db
  finally:
    db.close()