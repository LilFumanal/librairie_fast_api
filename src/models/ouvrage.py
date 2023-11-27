from datetime import date
from config import Base
from models import Commentaire
from sqlalchemy import Date, select, String, Text, Numeric, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship


class Ouvrage(Base):
    __tablename__ = "t_ouvrage"
    id_ouvrage: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titre_ouvrage: Mapped[str] = mapped_column(String(255))
    auteur_ouvrage: Mapped[str] = mapped_column(String(255))
    isbn_ouvrage: Mapped[str] = mapped_column(String(20))
    langue_ouvrage: Mapped[str] = mapped_column(String(20))
    prix_ouvrage: Mapped[float] = mapped_column(Float(10, 2))
    date_parution_ouvrage: Mapped[date] = mapped_column(Date)
    categorie_ouvrage: Mapped[str] = mapped_column(String(255))
    date_dispo_librairie_ouvrage: Mapped[date] = mapped_column(Date)
    date_dispo_particulier_ouvrage: Mapped[date] = mapped_column(Date)
    #image_ouvrage: Mapped[image] = mapped_column(object)
    table_matieres_ouvrage: Mapped[Text] = mapped_column(Text)
    mot_clef_ouvrage: Mapped[Text] = mapped_column(Text)
    description_ouvrage: Mapped[Text] = mapped_column(Text)
    
    commentaires_ouvrage: Mapped[list["Commentaire"]] = relationship(back_populates = "ouvrage")
