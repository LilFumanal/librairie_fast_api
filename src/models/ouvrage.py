from datetime import date
from config import Base
from sqlalchemy import select, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Ouvrage(Base):
    __tablename__ = "t_ouvrage"
    id_ouvrage: Mapped[int] = mapped_column(primary_key=True)
    titre_ouvrage: Mapped[str] = mapped_column(String(255))
    auteur_ouvrage: Mapped[str] = mapped_column(String(255))
    isbn_ouvrage: Mapped[str] = mapped_column(String(20))
    langue_ouvrage: Mapped[str] = mapped_column(String(20))
    prix_ouvrage: Mapped[float] = mapped_column(float(10, 2))
    date_parution_ouvrage: Mapped[date] = mapped_column(date)
    categorie_ouvrage: Mapped[str] = mapped_column(String(255))
    date_dispo_librairie_ouvrage: Mapped[date] = mapped_column(date)
    date_dispo_particulier_ouvrage: Mapped[date] = mapped_column(date)
    #image_ouvrage: Mapped[image] = mapped_column(object)
    table_matieres_ouvrage: Mapped[str] = mapped_column(String(255))
    mot_clef_ouvrage: Mapped[str] = mapped_column(String(255))
    description_ouvrage: Mapped[str] = mapped_column(String(255))
