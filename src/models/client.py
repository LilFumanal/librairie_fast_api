from config import Base
from typing import Optional
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship




class Client(Base):
    __tablename__ = "client"
    id_client: Mapped[int] = mapped_column(primary_key=True, autoincrement= True)
    nom_client: Mapped[str] =  mapped_column(String(255))
    prenom_client: Mapped[Optional[str]] =  mapped_column(String(255))
    email_client: Mapped[str] = mapped_column(String(255))
    telephone_client: Mapped[str] =  mapped_column(String(20))
    preferences_client: Mapped[Text] =  mapped_column(Text)
    adresse_livraison_client: Mapped[Text] =  mapped_column(Text)
    adresse_facturation_client: Mapped[Text] =  mapped_column(Text)
    
    commentaire_client: Mapped["Commentaire"] = relationship(back_populates="id_commentaire")

