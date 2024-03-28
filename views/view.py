
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
    
    def quit(self):
        print('--------------------------------------------------------------------')
        print('--------------------------Echec et Mat------------------------------')
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
        print('3 - Gérérer des rapports')
        print("9 - Quitter le programme")
        choice = None
        while choice not in ['1', '2', '3', '9']:
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
        print("9 - Quitter le programme")
        choice = None
        while choice not in ['1', '2', '3', '4', '5', '9']:
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
        print("9 - Quitter le programme")
        choice = None
        while choice not in ['1', '2', '3', '4', '5', '9']:
            choice = input('Votre choix : ')
        return int(choice)
    
    def addmember(self):
        choice = None
        while choice not in ['Quitter' or 'Oui']:
            print('--------------------------------------------------------------------')
            print('------------------------ Ajouter un membre -------------------------')
            print('--------------------------------------------------------------------')
            lastName = input('[Obligatoire] Nom de famille : ')
            firstName = input('[Obligatoire] Prénom : ')
            birthName = input('[Facultatif] Nom de naissance : ')
            nrFFE = input('[Obligatoire] Numéro FFE : ')
            elo = input('[Facultatif] Elo (Par défaut, il sera précisé 1000) :')
            
            print("\n\nVous confirmez l'enregistrement du joueur suivant dans la liste du club :")
            print(f'Nom de famille : {lastName}')
            print(f'Prénom : {firstName}')
            print(f'Nom de naissance : {birthName}')
            print(f'Numéro FFE : {nrFFE}')
            print(f'Elo : {elo}')
            
            while choice not in ['Oui', 'Non', 'Quitter']:
                choice = input("'Oui' / 'Non' / 'Quitter' : ")
        
            if choice == 'Oui':
                return lastName, firstName, birthName, nrFFE, elo
 
    def modifyConf(self):
        print("\n\nLe joueur est déja présent dans la liste des joueurs du club. Souhaitez vous le mettre à jour ? ")
        choice = None
        while choice not in ['Oui', 'Non']:
            choice = input("Votre choix 'Oui' / 'Non' : ")
        if choice == 'Oui':
            return True
        else: 
            return False


