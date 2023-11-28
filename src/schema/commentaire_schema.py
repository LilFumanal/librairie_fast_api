from datetime import date
from pydantic import BaseModel

class Commentaire(BaseModel):
    date_publication_commentaire: date
    commentaire: str
    titre_commentaire: str
    id_client: int
    id_ouvrage: int
    class Config:
        orm_mode = True

class CreatedCommentaire(Commentaire):
    id_commentaire: int
