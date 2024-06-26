

class View:
    def __init__(self):
        pass

    def accueil(self):
        print('--------------------------------------------------------------')
        print('--------------------------------------------------------------')
        print('-------------------------CHESS MASTER ------------------------')
        print('--------------------------------------------------------------')
        print('---------------------   _______________ ----------------------')
        print('---------------------8 |_|#|_|#|_|#|_|#|----------------------')
        print('---------------------7 |#|_|#|_|#|_|#|_|----------------------')
        print('---------------------6 |_|#|_|#|_|#|_|#|----------------------')
        print('---------------------5 |#|_|#|_|#|_|#|_|----------------------')
        print('---------------------4 |_|#|_|#|_|#|_|#|----------------------')
        print('---------------------3 |#|_|#|_|#|_|#|_|----------------------')
        print('---------------------2 |_|#|_|#|_|#|_|#|----------------------')
        print('---------------------1 |#|_|#|_|#|_|#|_|----------------------')
        print('---------------------   a b c d e f g h ----------------------')
        print('--------------------------------------------------------------')
        print('--------------------------------------------------------------')

    def quit(self):
        print('--------------------------------------------------------------')
        print('--------------------------Echec et Mat------------------------')
        print('--------------------------------------------------------------')

    def loading(self):
        print('---------------------Chargement du programme------------------')

    def data(self, tournamentId, roundId, matchId, totalClubPlayer):
        print('--------------------------------------------------------------')
        print('------------------------data importées------------------------')
        print(f'Tournois joués : {tournamentId}        ')
        print(f'Rounds joués : {roundId}        ')
        print(f'Matchs joués : {matchId}        ')
        print(f'Nombre de joueurs du cub : {totalClubPlayer}        ')
        print('--------------------------------------------------------------')

    def addmember(self):
        choice = None
        while choice not in ['Quitter' or 'Oui']:
            choice = "A"
            print('----------------------------------------------------------')
            print('------------------------ Ajouter un membre ---------------')
            print('----------------------------------------------------------')
            lastName = input('[Obligatoire] Nom de famille : ')
            firstName = input('[Obligatoire] Prénom : ')
            birthName = input('[Facultatif] Nom de naissance : ')
            nrFFE = input('[Obligatoire] Numéro FFE : ')
            elo = 1000
            while True:
                try:
                    user_input = input(
                        "[Facultatif] Elo (Par défaut : 1000) : ").strip()
                    if user_input == "":
                        break
                    elo = int(user_input)
                    break
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
            print("\n\nVous confirmez l'enregistrement du joueur",
                  "suivant dans la liste du club :")
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
        print("\n\nLe joueur est déja présent dans la liste des",
              " joueurs du club. Souhaitez vous le mettre à jour ? ")
        choice = None
        while choice not in ['Oui', 'Non']:
            choice = input("Votre choix 'Oui' / 'Non' : ")
        if choice == 'Oui':
            return True
        else:
            return False

    def modifyPlayer1(self):
        print('--------------------------------------------------------------')
        print("---------Modifier une caractéristique d'un membre ------------")
        print('--------------------------------------------------------------')
        print("\n\n Quel est le numéro FFE du Joueur ?")
        nrFfe = input('N°FFE : ')
        return nrFfe

    def modifyPlayer2(self, player):
        print("\n\n Quel est L'information à modifier :")
        print(f'1 - Nom de famille :    {player.lastName}')
        print(f'2 - Prénom :            {player.firstName}')
        print(f'3 - Nom de naissance :  {player.birthName}')
        print(f'4 - Elo :               {player.elo}')
        print('5 - Aucune')
        choice = None
        while choice not in ['1', '2', '3', '4', '5']:
            choice = input('Votre choix : ')
        return choice

    def modifyPlayer3(self):
        print("\n\n Il n'y a pas de joueur du club avec",
              " ce N° FFE, Quel est le numéro FFE du Joueur ?")
        nrFfe = input('N°FFE : ')
        return nrFfe

    def modifyPlayer4(self):
        print("\n\n Quelle est la nouvelle valeur ?")
        data = input(' Votre saisie : ')
        return data

    def startTournament(self):
        print('\n\n----------------------------------------------------------')
        print("--------------------Création d'un tournoi---------------------")

    def addPlayerAlreadyPresent(self):
        print("Joueur déjà présent dans le tournoi !")
        input("Appuyez sur Entrée pour continuer...")

    def createTournament(self):
        choice = None
        while choice not in ['Quitter' or 'Oui']:
            print('--------------------------------------------------------\n')
            name = input('[Obligatoire] Nom du tournoi : ')
            place = input('[Obligatoire] Lieu du tournoi : ')
            description = input('[Facultatif] Courte description : ')
            nrRound = 4
            while True:
                try:
                    user_input = input(
                        "[Facultatif] Nombre de tours (Par défaut 4): "
                        ).strip()
                    if user_input == "":
                        break
                    nrRound = int(user_input)
                    break
                except ValueError:
                    print("Veuillez entrer un nombre valide.")
            print("\n\nVous confirmez l'enregistrement du tournoi suivant :")
            print(f'Nom du tournoi : {name}')
            print(f'Lieu du tournoi : {place}')
            print(f'Description : {description}')
            print(f'Nombre de tours : {nrRound}')
            while choice not in ['Oui', 'Non', 'Quitter']:
                choice = input("'Oui' / 'Non' / 'Quitter' : ")
            if choice == 'Oui':
                return name, place, description, nrRound

    def confirmation(self, tournament):
        choice = None
        while choice not in ['Oui', 'Non']:
            print("\n\nATTENTION : Le lancement du tournoi",
                  " bloquera l'ajout de joueurs.")
            choice = input(
                "Avez vous associé tous les joueurs ? 'Oui' / 'Non' : ")
        if choice == 'Oui':
            return True
        else:
            return False

    def tournamentChoice(self, idList):
        print("\n\n Quel est l'id du tournoi que vous souhaitez continuer ? ")
        choice = None
        while choice not in idList:
            choice = int(input('Votre choix : '))
        return choice

    def modifyTournament(self, tournament):
        print("\n\n Quel est L'information à modifier :")
        print(f'1 - Nom du tournoi :    {tournament.name}')
        print(f'2 - Place :             {tournament.place}')
        print(f'3 - Descritpion :       {tournament.description}')
        print('6 - Aucune')
        choice = None
        data = None
        while choice not in ['1', '2', '3', '6']:
            choice = input('Votre choix : ')
        if choice != '6':
            data = input("quelle est la valeur à modifier?")
        return data, choice

    def blockAddPlayer(self):
        print("\n\n Ajout de joueur impossible, le tournoi a commencé")
        input("Appuyez sur Entrée pour continuer...")

    def maxRound(self):
        print("\n\n Nombre de tours max atteint.")
        input("Appuyez sur Entrée pour continuer...")

    def actualRoundNotFinished(self):
        print("\n\n Tour actuel n'est pas terminé, Merci d'entrer les scores.")
        input("Appuyez sur Entrée pour continuer...")

    def blockscores(self):
        print("\n\nEnregistrement impossible : pas de tour en cours")
        input("Appuyez sur Entrée pour continuer...")

    def blockvalidation(self):
        print("\n\nImpossible de terminer le tour, tous les scores ",
              "n'ont pas été intégrés")
        input("Appuyez sur Entrée pour continuer...")

    def scoresIntegration(self, tournament, nrRoundList):
        idMatch = None
        player1Score = None
        while idMatch not in nrRoundList:
            idMatch = int(input('\nId de match :'))
            print("\nQuel est le résultat pour le joueur 1 ?")
        while player1Score not in ['P', 'G', 'E']:
            player1Score = input(
                "A t'il gagné =>(G),perdu=>(P) ou égalité=>(E) : ")
        return idMatch, player1Score
