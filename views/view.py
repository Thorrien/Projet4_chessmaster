
class View:
    def __init__(self):
        pass
    
    
    def accueil(self):
        print('--------------------------------------------------------------------')
        print('--------------------------------------------------------------------')
        print('-------------------------CHESS MASTER ------------------------------')
        print('--------------------------------------------------------------------')       
        print('---------------------   _______________ ----------------------------')
        print('---------------------8 |_|#|_|#|_|#|_|#|----------------------------')
        print('---------------------7 |#|_|#|_|#|_|#|_|----------------------------')
        print('---------------------6 |_|#|_|#|_|#|_|#|----------------------------')
        print('---------------------5 |#|_|#|_|#|_|#|_|----------------------------')
        print('---------------------4 |_|#|_|#|_|#|_|#|----------------------------')
        print('---------------------3 |#|_|#|_|#|_|#|_|----------------------------')
        print('---------------------2 |_|#|_|#|_|#|_|#|----------------------------')
        print('---------------------1 |#|_|#|_|#|_|#|_|----------------------------')
        print('---------------------   a b c d e f g h ----------------------------')
        print('--------------------------------------------------------------------')
        print('--------------------------------------------------------------------')
        
    def loading(self):
        print('---------------------Chargement du programme------------------------')
        
    def data(self, tournamentId, roundId, matchId, totalClubPlayer):
        print('--------------------------------------------------------------------')
        print('------------------------data importées------------------------------')
        print(f'Tournois joués : {tournamentId}        ')
        print(f'Rounds joués : {roundId}        ')
        print(f'Matchs joués : {matchId}        ')   
        print(f'Nombre de joueurs du cub : {totalClubPlayer}        ')
        print('--------------------------------------------------------------------')
        
    def menu(self):
        print('--------------------------------------------------------------------')
        print('---------------------Que souhaitez vous faire ?---------------------')
        print('1 - Administrer le club et ses membres')
        print('2 - Gerer ou creer un tournoi')
        print('3 - ')
        choice = None
        while choice not in ['1', '2', '3']:
            choice = input('Votre choix : ')
        return int(choice)
    
    def administration(self):
        print('--------------------------------------------------------------------')
        print('-----------------Administrer le club et ses membres-----------------')
        print('---------------------Que souhaitez vous faire ?---------------------')
        print('1 - Ajouter un membre')
        print("2 - Modifier les données d'un membre")
        print('3 - Afficher la liste des membres')
        print("4 - Afficher l'historique du club")
        print("5 - Menu précédent")
        choice = None
        while choice not in ['1', '2', '3', '4', '5']:
            choice = input('Votre choix : ')
        return int(choice)
    
    def tournament(self):
        print('--------------------------------------------------------------------')
        print('----------------------Gerer ou creer un tournoi---------------------')
        print('---------------------Que souhaitez vous faire ?---------------------')
        print('1 - Creer un nouveau tournoi')
        print("2 - Reprendre un tournoi existant")
        print("3 - Afficher l'historique des tournois")
        print("4 - ")
        print("5 - Menu précédent")
        choice = None
        while choice not in ['1', '2', '3', '4', '5']:
            choice = input('Votre choix : ')
        return int(choice)