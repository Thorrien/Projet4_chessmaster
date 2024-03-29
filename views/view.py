from tabulate import tabulate


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
        print('\n\n--------------------------------------------------------------------')
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
        print("4 - Afficher l'historique des activités du club")
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
        print("4 - Menu précédent")
        print("9 - Quitter le programme")
        choice = None
        while choice not in ['1', '2', '3', '4', '9']:
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

    def modifyPlayer1(self):
        print('--------------------------------------------------------------------')
        print("---------Modifier une caractéristique d'un membre ------------------")
        print('--------------------------------------------------------------------')
        print("\n\n Quel est le numéro FFE du Joueur ?")        
        nrFfe = input('N°FFE : ')
        return nrFfe

    def modifyPlayer2(self, lastName, firstName, birthName, nrFFE, elo):
            print("\n\n Quel est L'information à modifier :")
            print(f'1 - Nom de famille :    {lastName}')
            print(f'2 - Prénom :            {firstName}')
            print(f'3 - Nom de naissance :  {birthName}')
            print(f'4 - Numéro FFE :        {nrFFE}')
            print(f'5 - Elo :               {elo}')
            print(f'6 - Aucune')
            choice = None
            while choice not in ['1', '2', '3', '4', '5', '6']:
                choice = input('Votre choix : ')
            return choice
        
    def modifyPlayer3(self):
        print("\n\n Il n'y a pas de joueur du club avec ce N° FFE, Quel est le numéro FFE du Joueur ?")        
        nrFfe = input('N°FFE : ')
        return nrFfe
    
    def modifyPlayer4(self):
        print("\n\n Quelle est la nouvelle valeur ?")        
        data = input(' Votre saisie : ')
        return data
    
    def printMember(self, table):
        print('\n\n--------------------------------------------------------------------')
        print("------------------Liste des joueurs du club-------------------------")
        print('--------------------------------------------------------------------')
        print(tabulate(table, headers="firstrow"))

    def activityList(self, table):
        print('\n\n--------------------------------------------------------------------')
        print("------------------Liste des joueurs du club-------------------------")
        print('--------------------------------------------------------------------')
        print(tabulate(table, headers="firstrow"))

    def rapports(self):
        print('--------------------------------------------------------------------')
        print('-------------------------Génerer un rapport-------------------------')
        print('----------------Quel rapport souhaitez vous générer ?---------------')
        print('1 - Liste de tous les joueurs par ordre alphabétique')
        print("2 - Liste de tous les tournois")
        print("3 - Informations d'un tournoi donné")
        print("4 - Liste des joueurs du tournoi par ordre alphabétique")
        print("5 - Liste de tous les tours du tournoi et de tous les matchs du tour")
        print('6 - Menu précédent')        
        print("9 - Quitter le programme")
        choice = None
        while choice not in ['1', '2', '3', '4', '5', '6', '9']:
            choice = input('Votre choix : ')
        return int(choice)