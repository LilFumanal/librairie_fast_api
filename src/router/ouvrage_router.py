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

@app.get("/ouvrage/{ouvrage.id}", response_model=ouvrage_schema.CreatedOuvrage)
def get_ouvrage_by_id(ouvrage_id: int, db: Session = Depends(get_db)):
  return db.query(Ouvrage).filter(Ouvrage.id_ouvrage == ouvrage_id).first()

@app.get("/ouvrage/{ouvrage.auteur}", response_model=ouvrage_schema.CreatedOuvrage)
def get_ouvrage_by_author(ouvrage_auteur: str, db: Session = Depends(get_db)):
  return db.query(Ouvrage).filter(Ouvrage.auteur_ouvrage == ouvrage_auteur).first()

@app.get("/ouvrage/{ouvrage.isbn}", response_model=ouvrage_schema.CreatedOuvrage)
def get_ouvrage_by_isbn(ouvrage_isbn: str, db: Session = Depends(get_db)):
  return db.query(Ouvrage).filter(Ouvrage.isbn_ouvrage == ouvrage_isbn).first()

@app.get("/ouvrage", response_model=list[ouvrage_schema.CreatedOuvrage])
def get_ouvrages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  return db.query(Ouvrage).offset(skip).limit(limit).all()

@app.post("/ouvrage", response_model=ouvrage_schema.Ouvrage)
def post_ouvrage(ouvrage: ouvrage_schema.Ouvrage, db: Session = Depends(get_db)):
  db_ouvrage = Ouvrage(titre_ouvrage = ouvrage.titre_ouvrage, auteur_ouvrage = ouvrage.auteur_ouvrage, isbn_ouvrage = ouvrage.isbn_ouvrage, langue_ouvrage = ouvrage.langue_ouvrage, prix_ouvrage = ouvrage.prix_ouvrage, date_parution_ouvrage = ouvrage.date_parution_ouvrage, categorie_ouvrage = ouvrage.categorie_ouvrage, date_dispo_librairie_ouvrage = ouvrage.date_dispo_librairie_ouvrage, date_dispo_particulier_ouvrage = ouvrage.date_dispo_particulier_ouvrage, table_matieres_ouvrage = ouvrage.table_matieres_ouvrage, mot_clef_ouvrage = ouvrage.mot_clef_ouvrage, description_ouvrage = ouvrage.description_ouvrage )
  db.add(db_ouvrage)
  db.commit()
  db.refresh(db_ouvrage)
  return db_ouvrage