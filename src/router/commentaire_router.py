# @app.post("/ouvrage", response_model=ouvrage_schema.CreateOuvrage)
# def post_ouvrage(db: Session, ouvrage: ouvrage_schema.CreateOuvrage):
#   db_ouvrage = Ouvrage(titre = ouvrage.titre, auteur = ouvrage.auteur, isbn = ouvrage.isbn, langue = ouvrage.langue, prix = ouvrage.prix, date_parution = ouvrage.date_parution, categorie = ouvrage.categorie, date_dispo_librairie = ouvrage.date_dispo_librairie, date_dispo_particulier = ouvrage.date_dispo_particulier, table_matières = ouvrage.table_matieres, mot_clef = ouvrage.mot_clef, description = ouvrage.description )
#   db.add(db_ouvrage)
#   db.commit()
#   db.refresh(db_ouvrage)
#   return db_ouvrage

from fastapi import APIRouter, Depends, FastAPI
from config import connexion
from models import Commentaire
from schema import commentaire_schema
from sqlalchemy.orm import Session

app = APIRouter()

def get_db():
  db = connexion.SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/commentaire/{commentaire.id}", response_model=commentaire_schema.CreatedCommentaire)
def get_commentaire_by_id(commentaire_id: int, db: Session = Depends(get_db)):
    return db.query(Commentaire).filter(Commentaire.id_commentaire == commentaire_id).first()       #Get commentaire via id du commentaire

@app.get("/commentaire/{ouvrage.id}", response_model=commentaire_schema.CreatedCommentaire)
def get_commentaire_by_ouvrage(ouvrage_id: int, db: Session = Depends(get_db)):
    return db.query(Commentaire).filter(Commentaire.id_ouvrage == ouvrage_id).first()       #Get commentaire via id ouvrage

@app.get("/commentaire/{client.id}", response_model=commentaire_schema.CreatedCommentaire)
def get_commentaire_by_client(client_id: int, db: Session = Depends(get_db)):
    return db.query(Commentaire).filter(Commentaire.id_client == client_id).first()         #Get commentaire via id client

@app.post("/commentaire", response_model=commentaire_schema.Commentaire)
def post_commentaire(commentaire: commentaire_schema.Commentaire, db: Session = Depends(get_db)):
    db_commentaire = Commentaire(date_publication_commentaire = commentaire.date_publication_commentaire, commentaire = commentaire.commentaire, titre_commentaire = commentaire.titre_commentaire)     #Créer un commentaire
    db.add(db_commentaire)
    db.commit()
    db.refresh(db_commentaire)
    return db_commentaire
