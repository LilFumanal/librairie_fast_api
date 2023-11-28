from pydantic import BaseModel
from . import commentaire_schema

class Client(BaseModel):
    nom_client: str
    prenom_client: str
    email_client: str
    telephone_client: str
    preferences_client: str
    adresse_livraison_client: str
    adresse_facturation_client: str
    
    class Config:
      orm_mode = True

class CreatedClient(Client):
  id_client: int