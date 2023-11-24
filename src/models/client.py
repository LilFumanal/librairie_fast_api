from config import Base
<<<<<<< Updated upstream
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text




class Client(Base):
    __tablename__ = "client"
    id_client: Mapped[int] = mapped_column(primary_key=True)
    nom_client: Mapped[str] =  mapped_column(String(255))
    prenom_client: Mapped[Optional[str]] =  mapped_column(String(255))
    email_client: Mapped[str] = mapped_column(String(255))
    telephone_client: Mapped[str] =  mapped_column(String(20))
    preferences_client: Mapped[Optional[str]] =  mapped_column(Text())
    adresse_livraison_client: Mapped[Optional[str]] =  mapped_column(Text())
    adresse_facturation_client: Mapped[Optional[str]] =  mapped_column(Text())
    
    

=======
from config import connexion as c


class Client(Base):
    pass




# CREATE TABLE Client (
#     id_client INT PRIMARY KEY AUTO_INCREMENT,
#     nom_client VARCHAR(255),
#     prenom_client VARCHAR(255),
#     email_client VARCHAR(255),
#     telephone_client VARCHAR(20),
#     preferences_client TEXT,
#     adresse_livraison_client TEXT,
#     adresse_facturation_client TEXT
# );
>>>>>>> Stashed changes
