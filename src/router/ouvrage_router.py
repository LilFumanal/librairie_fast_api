from fastapi import APIRouter, FastAPI
from models import Ouvrage
from schema import ouvrage_schema
from sqlalchemy.orm import Session

app = FastAPI()
router = APIRouter()

@app.get("/ouvrage/{ouvrage.id}", response_model=ouvrage_schema.Ouvrage)
def get_ouvrage_by_id(db: Session, ouvrage_id: int):
  return db.query(Ouvrage).filter(Ouvrage.id_ouvrage == ouvrage_id).first()

@app.get("/ouvrage/{ouvrage.auteur}", response_model=ouvrage_schema.Ouvrage)
def get_ouvrage_by_author(db: Session, ouvrage_auteur: str):
  return db.query(Ouvrage).filter(Ouvrage.auteur_ouvrage == ouvrage_auteur).first()

@app.get("/ouvrage/{ouvrage.isbn}", response_model=ouvrage_schema.Ouvrage)
def get_ouvrage_by_isbn(db: Session, ouvrage_isbn: str):
  return db.query(Ouvrage).filter(Ouvrage.isbn_ouvrage == ouvrage_isbn).first()

@app.get("/ouvrage", response_model=list[ouvrage_schema.Ouvrage])
def get_ouvrages(db: Session, skip: int = 0, limit: int = 100):
  return db.query(Ouvrage).offset(skip).limit(limit).all()