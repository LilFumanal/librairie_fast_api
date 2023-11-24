# from datetime import date
# from pydantic import BaseModel
# from . import commentaire_schema

# class Ouvrage(BaseModel):
#   titre: str
#   auteur: str
#   isbn: str
#   langue: str
#   prix: float
#   date_parution: date
#   categorie: str
#   date_dispo_librairie: date
#   date_dispo_particulier: date
#   table_matieres: str
#   mot_clef: str
#   description: str
  
# class CreateOuvrage(Ouvrage):
#   id: int
#   commentaire: list[Commentaire]
  
#   class Config:
#     orm_mode = True

from datetime import date
from pydantic import BaseModel

class Commentaire(BaseModel):



# id_commentaire: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
#     id_client: Mapped[int] = mapped_column(ForeignKey("client.id_client"))  #Clé étrangère Client
#     commentaires: Mapped["Client"] = relationship(back_populates="commentaires_client") #Relationship Client
#     id_ouvrage: Mapped[int] = mapped_column(ForeignKey("ouvrage.id_ouvrage"))   #Clé étrangère Ouvrage
#     ouvrage: Mapped["Ouvrage"] = relationship(back_populates="commentaires_ouvrage")    #Relationship Ouvrage
#     date_publication_commentaire: Mapped[date] = mapped_column(date)
#     commentaire: Mapped[str] = mapped_column(Text)
#     titre_commentaire: Mapped[str] = mapped_column(String(255))