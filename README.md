## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Couverture de test

- `pytest --cov=.`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

Le déploiement est mis en place avec une pipeline CI/CD en travaillant sur la branche `master`.

Le déploiement est réalisé en trois étapes:
- Tests unitaires et linting du code
- Si l'étape précédente est validée, une image Docker est créée et poussée sur DockerHub
- Si l'étape précédente est validée, le code est déployé dans Heroku

Les outils de CI/CD:
- Docker et DockerHub: Docker et DockerHub permettent de créer et stocker les images de notre application
- CircleCI: permet de mettre en place le pipeline (exécution des étapes de CI/CD)
- Heroku: permet d'héberger notre application et de la rendre accessible publiquement

La configuration requise pour que le déploiement fonctionne correctement:
- Les tests unitaires et linting de code ne doivent pas remonter des erreurs
- La couverture du code doit être superieur à 80%
- L'image docker doit être crée correctemment et envoyé correctement sur DockerHub
- Les variables d'environnment doivent être definis sur Heroku

Les étapes à suivre pour effectuer le déploiement:
- Créer une branche pour réaliser des corrections ou améliorations (ne pas travailler dans branch master directement)
- Ajouter les tests unitaires si nécessaire
- Réaliser le commit et push de cette nouvelle branche
- Voir les logs dans CircleCI pour avoir un retour pour les tests et linting
- Si tous les feux verts sont ok, vous pouvez merger vos modifications dans la branche `master` et faire un push
- Voir les logs dans CircleCI pour avoir un retour pour les tests, linting, création de l'image et le déploiement sur Heroku