# BetPlatform

## Table des Matières
- [Aperçu](#aperçu)
- [Architecture](#architecture)
- [Mise en Place](#mise-en-place)
  - [Prérequis](#prérequis)
  - [Installation](#installation)
  - [Lancement pour dev](#lancement-pour-dev)
- [Licence](#licence)

## Aperçu

BetPlatform est une application de paris sportifs construite avec [FastAPI](https://fastapi.tiangolo.com/) côté serveur et [Vue.js](https://vuejs.org/) côté client. L'objectif de ce projet est de fournir un guide rapide pour démarrer et d'expliquer les aspects clés de l'application.

## Architecture

L'architecture du projet est divisée en deux parties principales :
- **Backend** : Le serveur FastAPI gère les données des utilisateurs, des paris et des matchs, ainsi que l'authentification via JWT.
- **Frontend** : L'interface utilisateur construite avec Vue.js permet aux utilisateurs de s'inscrire, de se connecter, de placer des paris et de consulter le classement des joueurs.

## Mise en Place

### Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre système :

- [Python](https://www.python.org/) (3.7+)
- [Node.js](https://nodejs.org/) (avec npm)
- [Vue CLI](https://cli.vuejs.org/guide/installation.html)
- [PostgreSQL](https://www.postgresql.org/)

### Installation

1. Clonez le dépôt Git vers votre machine locale :

```bash
git clone https://github.com/TheoLaperrouse/BetPlatform
```
2. Configurer les variables d'environnement:
```
DATABASE_URL=postgresql://user:password@localhost:5432/betplatform
JWT_SECRET_KEY=SECRET_KET
JWT_EXPIRATION_TIME=720
```
3. Lancer le docker-compose:
```
docker-compose up
```

### Lancement pour dev:

Lancement back en local
```sh
poetry install
poetry run uvicorn app.main:app --host 0.0.0.0 --port 5000 --reload
```

Lancement front en local
```sh
yarn
yarn start 
```

### Licence
Ce projet est sous licence MIT. Veuillez consulter le fichier LICENSE pour plus d'informations.