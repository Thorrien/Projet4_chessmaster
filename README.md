# Projet ChessMaster

Ce projet est un système de gestion de tournois d'échecs appelé ChessMaster. Il permet de créer, de gérer et de suivre des tournois d'échecs, ainsi que de gérer les joueurs et les parties.

## Configuration

1. Assurez-vous d'avoir Python installé sur votre système. Vous pouvez télécharger Python depuis [le site officiel](https://www.python.org/).

2. Clonez ce dépôt sur votre machine locale :

```bash
git clone https://github.com/Thorrien/Projet4_chessmaster.git
```

3. Installez les dépendances requises à partir du fichier requirements.txt :

```bash
pip install -r requirements.txt
```

## Utilisation

En ayant l'environement virtuel d'actif, pour lancer le programme, exécutez le fichier main.py :

```bash
python main.py
```
Cela lancera le programme ChessMaster, où vous pourrez accéder aux différentes fonctionnalités via un menu interactif.

## Générer un rapport Flake8 HTML

En ayant l'environement virtuel d'actif, pour générer un nouveau rapport HTML à partir de Flake8, suivez les étapes suivantes :

1. Exécutez Flake8 sur votre projet pour générer le rapport. Vous pouvez spécifier le format de sortie en utilisant l'option --format. Pour générer un rapport au format HTML, utilisez la commande suivante :
   
   ```bash
    flake8 --exclude=env --format=html --htmldir=flake8_reports
    ```

2. Cela générera un nouveau dossier flake8-report dans votre répertoire de projet contenant le fichier HTML du rapport. Vous pouvez maintenant ouvrir ce fichier dans votre navigateur pour consulter les résultats du linter.


## Fonctionnalités

- Créer, modifier et afficher des tournois.
- Ajouter, modifier et afficher des joueurs.
- Gérer les parties et les rounds de tournois.
- Afficher des rapports sur les tournois et les joueurs.

## Contributeurs

- BARILLER Eric