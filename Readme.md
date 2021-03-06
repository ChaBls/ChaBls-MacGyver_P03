# Aidez MacGyver à s'échapper!
***
Ce projet OpenClassRooms est un jeu sous forme de labyrinthe, codé en langage Python.
MacGyver (incarné par le joueur) doit trouver trois items afin de concevoir
une seringue à l'aide de laquelle il endormira le gardien pour s'échapper.
[En savoir plus sur le projet](https://openclassrooms.com/fr/projects/aidez-macgyver-a-sechapper/assignment)
***
## Installation
***
Voici les étapes d'installation du jeu, sous environnement 'Pipenv'
***
* Installer pip3
* Installer pipenv
* Importer le projet à partir du dépôt
* Se positionner dans la copie du dépôt
* Installer les dépendances (à l'aide de Pipfile)
* Activer l'environnement virtuel
* Lancer le jeu
```
$ sudo apt-get install pip3
$ pip3 install pipenv
$ git clone https://github.com/ChaBls/ChaBls-MacGyver_P03
$ cd path/to/ChaBls-MacGyver_P03
$ pipenv install
$ pipenv shell
$ pipenv run python3 main.py
```
***
### Consignes
***
* Utilisez les flèches directionnelles pour déplacer MacGyver
* La fenêtre du jeu peut être fermée à tout moment en cliquant sur la croix
prévue à cet effet, ou bien en appuyant sur 'ECHAP'
***
#### But du jeu
Vous incarnez MacGyver, bloqué dans un labyrinthe.
Afin d'endormir le gardien qui vous retient prisonnier, voici ce que vous devez trouver :
* Un tube en plastique
* Une aiguille
* Un flacon d'éther
***
[Code source du projet](https://github.com/ChaBls/ChaBls-MacGyver_P03)