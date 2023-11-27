from datetime import date
from pydantic import BaseModel
from . import commentaire_schema

class Ouvrage(BaseModel):
  titre: str
  auteur: str
  isbn: str
  langue: str
  prix: float
  date_parution: date
  categorie: str
  date_dispo_librairie: date
  date_dispo_particulier: date
  table_matieres: str
  mot_clef: str
  description: str
  
  class Config:
    orm_mode = True
class CreateOuvrage(Ouvrage):
  id: int