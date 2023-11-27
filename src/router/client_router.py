from fastapi import APIRouter, FastAPI
from models import Client
from schema import client_schema
from sqlalchemy.orm import Session

app = FastAPI()
router = APIRouter()

@app.get("/client/{client.id}", response_model=client_schema.Client)
def get_client_by_id(db: Session, client_id: int):
  return db.query(Client).filter(Client.id_client == client_id).first()

@app.get("/client/{client.nom}", response_model=client_schema.Client)
def get_client_by_nom(db: Session, client_nom: str):
  return db.query(Client).filter(Client.nom_client == client_nom).first()

@app.get("/client/{client.prenom}", response_model=client_schema.Client)
def get_client_by_prenom(db: Session, client_prenom: str):
  return db.query(Client).filter(Client.prenom_client == client_prenom).first()

@app.get("/client", response_model=list[client_schema.Client])
def get_clients(db: Session, skip: int = 0, limit: int = 100):
  return db.query(Client).offset(skip).limit(limit).all()

@app.post("/client", response_model=client_schema.CreateClient)
def post_client(db: Session, client: client_schema.CreateClient):
  db_client = Client(nom = client.nom, prenom = client.prenom, email = client.email, telephone = client.telephone, preferences = client.preferences, adresse_livraison = client.adresse_livraison, adresse_facturation = client.adresse_facturation )
  db.add(db_client)
  db.commit()
  db.refresh(db_client)
  return db_client