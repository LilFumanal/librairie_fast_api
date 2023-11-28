from pydantic import BaseModel
from . import commentaire_schema

class Client(BaseModel):
    nom: str
    prenom: str
    email: str
    telephone: str
    preferences: str
    adresse_livraison: str
    adresse_facturation: str
    
    class Config:
     orm_mode = True

class CreateOuvrage(Ouvrage):
  id: int