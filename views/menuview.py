

class MenuView:
    def __init__(self):
        pass

    def rapports(self):
        print('-----------------------------------------------------------')
        print('-------------------------Génerer un rapport----------------')
        print('----------------Quel rapport souhaitez vous générer ?------')
        print('1 - Liste de tous les joueurs par ordre alphabétique')
        print("2 - Liste de tous les tournois")
        print("3 - Informations d'un tournoi donné")
        print("4 - Liste des joueurs d'un tournoi par ordre alphabétique")
        print("5 - Liste de tous les tours d'un tournoi et de tous les ",
              "matchs du tour")
        print('6 - Menu principal')
        print("9 - Quitter le programme")
        choice = None
        while choice not in ['1', '2', '3', '4', '5', '6', '9']:
            choice = input('Votre choix : ')
        return int(choice)

    def menu(self):
        print('\n\n---------------------------------------------------------')
        print('---------------------Que souhaitez vous faire ?------------')
        print('1 - Administrer le club et ses membres')
        print('2 - Gerer ou creer un tournoi')
        print('3 - Gérérer des rapports')
        print("9 - Quitter le programme")
        choice = None
        while choice not in ['1', '2', '3', '9']:
            choice = input('Votre choix : ')
        return int(choice)

    def administration(self):
        print('-----------------------------------------------------------')
        print('-----------------Administrer le club et ses membres--------')
        print('---------------------Que souhaitez vous faire ?------------')
        print('1 - Ajouter un membre')
        print("2 - Modifier les données d'un membre")
        print('3 - Afficher la liste des membres')
        print("4 - Afficher l'historique des activités du club")
        print("5 - Menu principal")
        print("9 - Quitter le programme")
        choice = None
        while choice not in ['1', '2', '3', '4', '5', '9']:
            choice = input('Votre choix : ')
        return int(choice)

    def tournament(self):
        print('-----------------------------------------------------------')
        print('----------------------Gerer ou creer un tournoi------------')
        print('---------------------Que souhaitez vous faire ?------------')
        print('1 - Creer un nouveau tournoi')
        print("2 - Reprendre un tournoi existant")
        print("3 - Afficher l'historique des tournois")
        print("4 - Menu principal")
        print("9 - Quitter le programme")
        choice = None
        while choice not in ['1', '2', '3', '4', '9']:
            choice = input('Votre choix : ')
        return int(choice)

    def choiceDriveTournament(self, tournament):
        print(f'                           {tournament.name}')
        print('\n---------------------Que souhaitez vous faire ?------------')
        print('1 - Modifier les informations')
        print("2 - Ajouter des joueurs")
        print("3 - Lancer le tour suivant")
        print("4 - Entrer des scores du tour en cours")
        print("5 - Voir les scores globaux")
        print("6 - Menu principal")
        print("9 - Quitter le programme")
        choice = None
        while choice not in ['1', '2', '3', '4', '5', '6', '9']:
            choice = input('Votre choix : ')
        return int(choice)

    def scoresTypeIntegration(self, tournament):
        print('\n---------------------Que souhaitez vous faire ?------------')
        print('1 - Entrer un score')
        print("2 - Terminer le tour")
        print("3 - Jouer aléatoirement les matchs")
        print("4 - Menu précédent")
        print("9 - Quitter le programme")
        choice = None
        while choice not in ['1', '2', '3', '4', '9']:
            choice = input('Votre choix : ')
        return int(choice)
