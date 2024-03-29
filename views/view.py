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
    
    def startTournament(self):
        print('\n\n--------------------------------------------------------------------')
        print("--------------------Création d'un tournoi---------------------------")

        
        
        
    def  createTournament(self):
        choice = None
        while choice not in ['Quitter' or 'Oui']:
            print('--------------------------------------------------------------------\n')
            name = input('[Obligatoire] Nom du tournoi : ')
            place = input('[Obligatoire] Lieu du tournoi : ')
            description = input('[Facultatif] Courte description : ')
              
            print("\n\nVous confirmez l'enregistrement du joueur suivant dans la liste du club :")
            print(f'Nom du tournoi : {name}')
            print(f'Lieu du tournoi : {place}')
            print(f'Description : {description}')
            
            while choice not in ['Oui', 'Non', 'Quitter']:
                choice = input("'Oui' / 'Non' / 'Quitter' : ")
        
            if choice == 'Oui':
                return name, place, description 
      
            
    def tournamentChoice(self, idList):
        print("\n\n Quel est l'id du tournoi que vous souhaitez continuer ?")        
        choice = None
        while choice not in idList:
            choice = int(input('Votre choix : '))
        return choice
    
