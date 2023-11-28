
# projet librairie FastAPI

## Description
Ce projet a été réalisé dans le cadre de notre formation Concepteur Développeur d'Applications Python chez Diginamic. Le but est de créer et initialiser une base de données pour une librairie, qui permet de stocker et traiter des informations sur les clients, les ouvrages ainsi que les commentaires sur ceux-ci.

## Fonctionnalités
- L'application utilise le framework FastAPI pour interagir avec la base de données.
- Elle se connecte à une base de données MySQL à l'aide de la librairie pyMySQL.
- La gestion de l'ORM est assurée par la librairie SqlAlchelmy.
- Les tests unitaires sont mis en place avec le module unittest.
- Le serveur d'application est démarré à l'aide de la librairie Uvicorn.

## Architecture du Projet
Le projet suit une structure standard pour un projet Python. Voici un aperçu :
```
nom_projet/
    |- README.md
    |- requirements.txt
    |- setup.py
    |- .gitignore
    |- src/
        |- __init__.py
        |- main.py
        |- models/
            |- __init__.py
            |- ...
        |- routes/
            |- __init__.py
            |- ...
        |- schemas/
            |- __init__.py
            |- ...
        |- config/
            |- __init__.py
            |- connexion.py
            |- ...
    |- tests/
        |- __init__.py
        |- ...

```
- Le dossier `src/` contient le code source de l'application, avec ses différents modules.
- Les tests unitaires sont placés dans le dossier `tests/`.

## Installation
1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir **Python 3.9** installé sur votre système.
3. Créez un environnement virtuel et activez-le.
4. À l'intérieur de l'environnement virtuel, exécutez la commande suivante pour installer les dépendances du projet :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation
1. Assurez-vous que votre environnement virtuel est activé.
2. Accédez au répertoire du projet.
3. Exécutez la commande suivante pour démarrer le serveur d'application :
   ```bash
   uvicorn main:app --reload
   ```
   Cela lancera le serveur d'application sur `http://localhost:8000`.

## Contributions
Ce projet a été développé par [Lil Fumanal](https://github.com/LilFumanal), [Pierrick Le Bras](https://github.com/Pierrick-LB) et [Stefan de Kok](https://github.com/FentasKodek).

## Commandes
Ajouter une dépendance au projet :
```bash
pip freeze > requirements.txt
```