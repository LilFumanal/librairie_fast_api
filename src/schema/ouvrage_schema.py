from datetime import date
from pydantic import BaseModel
from . import commentaire_schema

class Ouvrage(BaseModel):
  titre_ouvrage: str
  auteur_ouvrage: str
  isbn_ouvrage: str
  langue_ouvrage: str
  prix_ouvrage: float
  date_parution_ouvrage: date
  categorie_ouvrage: str
  date_dispo_librairie_ouvrage: date
  date_dispo_particulier_ouvrage: date
  table_matieres_ouvrage: str
  mot_clef_ouvrage: str
  description_ouvrage: str
  
  class Config:
    orm_mode = True
class CreatedOuvrage(Ouvrage):
  id_ouvrage: int
  commentaire: list[commentaire_schema.Commentaire] = []
