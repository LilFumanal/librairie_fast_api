from models import Client, Ouvrage
from datetime import date
from config import Base
from sqlalchemy import ForeignKey, select, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

class Commentaire:
    __tablename__ = "t_commentaire"
    id_commentaire: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_client: Mapped[int] = mapped_column(ForeignKey("client.id_client"))  #Clé étrangère Client
    commentaires: Mapped["Client"] = relationship(back_populates="commentaires_client") #Relationship Client
    id_ouvrage: Mapped[int] = mapped_column(ForeignKey("ouvrage.id_ouvrage"))   #Clé étrangère Ouvrage
    ouvrage: Mapped["Ouvrage"] = relationship(back_populates="commentaires_ouvrage")    #Relationship Ouvrage
    date_publication_commentaire: Mapped[date] = mapped_column(date)
    commentaire: Mapped[str] = mapped_column(Text)
    titre_commentaire: Mapped[str] = mapped_column(String(255))

#     parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
#     parent: Mapped["Parent"] = relationship(back_populates="children")