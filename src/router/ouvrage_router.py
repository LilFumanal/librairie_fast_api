from fastapi import APIRouter, Depends, FastAPI
from models import Ouvrage
from schema import ouvrage_schema
from sqlalchemy.orm import Session
from config import connexion

app = APIRouter()

# Dependency
def get_db():
  db = connexion.SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/ouvrage/{ouvrage.id}", response_model=ouvrage_schema.Ouvrage)
def get_ouvrage_by_id(ouvrage_id: int, db: Session = Depends(get_db)):
  return db.query(Ouvrage).filter(Ouvrage.id_ouvrage == ouvrage_id).first()

@app.get("/ouvrage/{ouvrage.auteur}", response_model=ouvrage_schema.Ouvrage)
def get_ouvrage_by_author(ouvrage_auteur: str, db: Session = Depends(get_db)):
  return db.query(Ouvrage).filter(Ouvrage.auteur_ouvrage == ouvrage_auteur).first()

@app.get("/ouvrage/{ouvrage.isbn}", response_model=ouvrage_schema.Ouvrage)
def get_ouvrage_by_isbn(ouvrage_isbn: str, db: Session = Depends(get_db)):
  return db.query(Ouvrage).filter(Ouvrage.isbn_ouvrage == ouvrage_isbn).first()

@app.get("/ouvrage", response_model=list[ouvrage_schema.Ouvrage])
def get_ouvrages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  return db.query(Ouvrage).offset(skip).limit(limit).all()

@app.post("/ouvrage", response_model=ouvrage_schema.CreateOuvrage)
def post_ouvrage(ouvrage: ouvrage_schema.CreateOuvrage, db: Session = Depends(get_db)):
  db_ouvrage = Ouvrage(titre = ouvrage.titre, auteur = ouvrage.auteur, isbn = ouvrage.isbn, langue = ouvrage.langue, prix = ouvrage.prix, date_parution = ouvrage.date_parution, categorie = ouvrage.categorie, date_dispo_librairie = ouvrage.date_dispo_librairie, date_dispo_particulier = ouvrage.date_dispo_particulier, table_matières = ouvrage.table_matieres, mot_clef = ouvrage.mot_clef, description = ouvrage.description )
  db.add(db_ouvrage)
  db.commit()
  db.refresh(db_ouvrage)
  return db_ouvrage