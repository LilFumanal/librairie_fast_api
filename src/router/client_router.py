from fastapi import APIRouter, Depends, FastAPI
from models import Client
from schema import client_schema
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

@app.get("/client/{client.id}", response_model=client_schema.Client)
def get_client_by_id(client_id: int, db: Session = Depends(get_db)):
  return db.query(Client).filter(Client.id_client == client_id).first()

@app.get("/client/{client.nom}", response_model=client_schema.Client)
def get_client_by_nom(client_nom: str, db: Session = Depends(get_db)):
  return db.query(Client).filter(Client.nom_client == client_nom).first()

@app.get("/client/{client.prenom}", response_model=client_schema.Client)
def get_client_by_prenom(client_prenom: str, db: Session = Depends(get_db)):
  return db.query(Client).filter(Client.prenom_client == client_prenom).first()

@app.get("/client", response_model=list[client_schema.Client])
def get_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  return db.query(Client).offset(skip).limit(limit).all()

@app.post("/client", response_model=client_schema.CreateClient)
def post_client(client: client_schema.CreateClient, db: Session = Depends(get_db)):
  db_client = Client(nom = client.nom, prenom = client.prenom, email = client.email, telephone = client.telephone, preferences = client.preferences, adresse_livraison = client.adresse_livraison, adresse_facturation = client.adresse_facturation )
  db.add(db_client)
  db.commit()
  db.refresh(db_client)
  return db_client