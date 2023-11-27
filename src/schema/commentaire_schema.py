from datetime import date
from pydantic import BaseModel

class Commentaire(BaseModel):
    date_publication_commentaire: date
    commentaire: str
    titre_commentaire: str

    class Config:
        orm_mode = True

class CreateCommentaire(Commentaire):
    id: int
    id_client: int
    id_ouvrage: int
