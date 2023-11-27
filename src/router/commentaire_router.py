# @app.post("/ouvrage", response_model=ouvrage_schema.CreateOuvrage)
# def post_ouvrage(db: Session, ouvrage: ouvrage_schema.CreateOuvrage):
#   db_ouvrage = Ouvrage(titre = ouvrage.titre, auteur = ouvrage.auteur, isbn = ouvrage.isbn, langue = ouvrage.langue, prix = ouvrage.prix, date_parution = ouvrage.date_parution, categorie = ouvrage.categorie, date_dispo_librairie = ouvrage.date_dispo_librairie, date_dispo_particulier = ouvrage.date_dispo_particulier, table_matières = ouvrage.table_matieres, mot_clef = ouvrage.mot_clef, description = ouvrage.description )
#   db.add(db_ouvrage)
#   db.commit()
#   db.refresh(db_ouvrage)
#   return db_ouvrage

from fastapi import APIRouter, FastAPI
from models import Commentaire
from schema import commentaire_schema
from sqlalchemy.orm import Session

app = APIRouter

@app.get("/commentaire/{commentaire.id}", response_model=commentaire_schema.Commentaire)
def get_commentaire_by_id(db: Session, commentaire_id: int):
    return db.query(Commentaire).filter(Commentaire.id_commentaire == commentaire_id).first()       #Get commentaire via id du commentaire

@app.get("/commentaire/{ouvrage.id}", response_model=commentaire_schema.Commentaire)
def get_commentaire_by_ouvrage(db: Session, ouvrage_id: int):
    return db.query(Commentaire).filter(Commentaire.id_ouvrage == ouvrage_id).first()       #Get commentaire via id ouvrage

@app.get("/commentaire/{client.id}", response_model=commentaire_schema.Commentaire)
def get_commentaire_by_client(db: Session, client_id: int):
    return db.query(Commentaire).filter(Commentaire.id_client == client_id).first()         #Get commentaire via id client

@app.post("/commentaire", response_model=commentaire_schema.CreateCommentaire)
def post_commentaire(db: Session, commentaire: commentaire_schema.CreateCommentaire):
    db_commentaire = Commentaire(date = commentaire.date_publication_commentaire, com = commentaire.commentaire, titre = commentaire.titre_commentaire)     #Créer un commentaire
    db.add(db_commentaire)
    db.commit()
    db.refresh(db_commentaire)
    return db_commentaire
