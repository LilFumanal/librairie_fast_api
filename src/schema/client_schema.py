from pydantic import BaseModel


class Client(BaseModel):
    nom: str
    prenom: str
    email: str
    telephone: str
    preferences: str
    adresse_livraison: str
    adresse_facturation: str