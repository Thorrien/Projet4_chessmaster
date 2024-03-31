from models.tournament import Tournament

class TournamentManager:
    def __init__(self):
        pass
    
    def createTournament(self, view, saverLoader):
        view.startTournament()
        name, place, description = view.createTournament()
        tournament = Tournament(name, place)
        tournament.description = description
        print('Tournoi créé !')
        saverLoader.saveTournament(tournament)
        saverLoader.saveData()
            
            
    def printAllTournament(self, saverLoader, rapportView):
        idList = []
        tournaments = saverLoader.loadAllTournament()
        print(tournaments)

        tournaments.sort(key=lambda tournament: tournament.startDate, reverse=True)
        table = [['Date', 'id', 'Nom du tournoi', 'Etat', 'tours', 'Nombre de joueurs']]
        for tournament in tournaments:
            if tournament.endDate:
                etat = 'Terminé'
                idList.append(tournament.id)
            else: 
                etat = 'En cours'
                idList.append(tournament.id)
            table.append([tournament.startDate, tournament.id, tournament.name, etat, f'{tournament.actualRound} / {tournament.nrRound}', len(tournament.playerList)])
        rapportView.tournamentsList(table)
        idList.append(tournament.id)
        return idList
        
        
    def printActivesTournament(self, saverLoader, rapportView):
        idList = []
        tournaments = saverLoader.loadAllTournament()
        tournaments.sort(key=lambda tournament: tournament.startDate, reverse=True)
        table = [['Date', 'id', 'Nom du tournoi', 'Etat', 'tours', 'Nombre de joueurs']]
        for tournament in tournaments:
            if tournament.endDate:
                etat = 'Terminé'
            else: 
                etat = 'En cours'
                table.append([tournament.startDate, tournament.id, tournament.name, etat, f'{tournament.actualRound} / {tournament.nrRound}', len(tournament.playerList)])
                idList.append(tournament.id)
        rapportView.tournamentsACList(table)
        return idList

    def continueTournament(self, saverLoader, view, rapportView):
        idList = self.printActivesTournament(saverLoader, rapportView)
        choice = view.tournamentChoice(idList)
        return choice
    
    def manageTournament(self,saverLoader, view, rapportView, menuView, choice):
        tournament = saverLoader.loadSpecificTournament(choice)
        table = [[ 'id', 'Nom du tournoi', 'Date', 'tours']]
        table.append([tournament.id, tournament.name, tournament.startDate, f'{tournament.actualRound} / {tournament.nrRound}'])
        table2 = [['Nom', 'Prénom', 'score', 'Nom de naissance', 'N°FFE', 'Elo']]
        tournament.playerList.sort(key=lambda player: player[0].firstName)
        tournament.playerList.sort(key=lambda player: player[0].lastName)
        for player in tournament.playerList:
            table2.append([player[0].lastName, player[0].firstName, player[1], player[0].birthName, player[0].nrFFE, player[0].elo])
        rapportView.driveTournament(tournament)
        choice = menuView.choiceDriveTournament(tournament)
        return tournament, choice
        
    def modifyTournament(self, saverLoader, view, rapportView, tournament):
        data, choice = view.modifyTournament(tournament)
        if data is not None or choice != '6':
            if choice == '1':
                tournament.name = data
            if choice == '2':
                tournament.place = data
            if choice == '3':
                tournament.description = data
        saverLoader.updateTournament(tournament)
        
    def addPlayerTournament(self, saverLoader, view, rapportView, tournament):
        nrFFE = None
        while nrFFE != 'Terminé':
            table = [['N°FFE', 'Nom', 'Prénom', 'Nom de naissance', 'Elo']]
            playerList = saverLoader.loadAllPlayers()
            playerList.sort(key=lambda player: player.firstName)
            playerList.sort(key=lambda player: player.lastName)     
            FFEList = ['Terminé']
            FFEList2 = []
            for player in playerList:
                FFEList.append(player.nrFFE)
                table.append([player.nrFFE, player.lastName, player.firstName, player.birthName, player.elo])
            table2 = [['Nom', 'Prénom', 'score', 'Nom de naissance', 'N°FFE', 'Elo']]
            if len(tournament.playerList) != 0:
                tournament.playerList.sort(key=lambda player: player[0].firstName)
                tournament.playerList.sort(key=lambda player: player[0].lastName)
                for player in tournament.playerList:
                    FFEList2.append(player[0].nrFFE)
                    table2.append([player[0].lastName, player[0].firstName, player[1], player[0].birthName, player[0].nrFFE, player[0].elo])
            nrFFE = None
            nrFFE = rapportView.addPlayer(table, table2, tournament, FFEList)
            if nrFFE != 'Terminé': 
                playeradded = saverLoader.getPlayerFromJson(nrFFE)
                if nrFFE in FFEList2:
                    view.addPlayerAlreadyPresent()
                else :
                    tournament.addPayerList(playeradded)
                    saverLoader.updateTournament(tournament)
            else: 
                nrFFE = 'Terminé'
            

    def printspecifictournament(self, saverLoader, view, rapportView):
        idList = self.printAllTournament(saverLoader, rapportView)
        choice = view.tournamentChoice(idList)
        tournament = saverLoader.loadSpecificTournament(choice)
        tables= []
        if tournament.endDate:
            etat = 'Terminé'
        else: 
            etat = 'En cours'
        table = [[ 'id', 'Nom du tournoi', 'Date', 'tours', 'Etat']]
        table.append([tournament.id, tournament.name, tournament.startDate, f'{tournament.actualRound} / {tournament.nrRound}', etat])
        table2 = [['Nom', 'Prénom', 'score', 'Nom de naissance', 'N°FFE', 'Elo']]
        tournament.playerList.sort(key=lambda player: player[0].firstName)
        tournament.playerList.sort(key=lambda player: player[0].lastName)
        for player in tournament.playerList:
            table2.append([player[0].lastName, player[0].firstName, player[1], player[0].birthName, player[0].nrFFE, player[0].elo])
        table3 = [["id", "Nom du Tour", "Date de début", "Nombre de match", "Date de fin"]]
        table4 = [["Tour", "Id du match", "Joueur 1", "Joueur 2", "Score"]]
        for round in tournament.roundList:
            table4 = [["Tour", "Id ", "Date", "Joueur 1", "Joueur 2", "Score"]]
            table3.append([round.id, round.name, round.startDate, len(round.matchList), round.endDate])
            for match in round.matchList:
                table4.append([round.name, match.id, f"{match.duo[0][0].nrFFE} : {match.duo[0][0].lastName}  {match.duo[0][0].firstName} ({match.duo[0][0].elo})", f"{match.duo[1][0].nrFFE} : {match.duo[1][0].lastName}  {match.duo[1][0].firstName} ({match.duo[1][0].elo})", f"{match.duo[0][1]}/{match.duo[1][1]}"])
            tables.append(table4)
        rapportView.printTournament(table, table2, table3, tables, tournament)
        
    def playerListOfASpecificTournament(self, saverLoader, view, rapportView):
        idList = self.printAllTournament(saverLoader, rapportView)
        choice = view.tournamentChoice(idList)
        tournament = saverLoader.loadSpecificTournament(choice)
        table2 = [['Nom', 'Prénom', 'score', 'Nom de naissance', 'N°FFE', 'Elo']]
        tournament.playerList.sort(key=lambda player: player[0].firstName)
        tournament.playerList.sort(key=lambda player: player[0].lastName)
        for player in tournament.playerList:
            table2.append([player[0].lastName, player[0].firstName, player[1], player[0].birthName, player[0].nrFFE, player[0].elo])
        rapportView.printPlayerListTournament(table2, tournament)
    
    def matchListOfASpecificTournament(self, saverLoader, view, rapportView):
        idList = self.printAllTournament(saverLoader, rapportView)
        choice = view.tournamentChoice(idList)
        tournament = saverLoader.loadSpecificTournament(choice)
        tables = []
        table4 = [["Tour", "Id du match", "Joueur 1", "Joueur 2", "Score"]]
        for round in tournament.roundList:
            table4 = [["Tour", "Id ", "Date", "Joueur 1", "Joueur 2", "Score"]]
            for match in round.matchList:
                table4.append([round.name, match.id, f"{match.duo[0][0].nrFFE} : {match.duo[0][0].lastName}  {match.duo[0][0].firstName} ({match.duo[0][0].elo})", f"{match.duo[1][0].nrFFE} : {match.duo[1][0].lastName}  {match.duo[1][0].firstName} ({match.duo[1][0].elo})", f"{match.duo[0][1]}/{match.duo[1][1]}"])
            tables.append(table4)
        rapportView.printMatchListTournament(tables, tournament)
        
    def runNextTournament(self, saverLoader, tournament):
        tournament.createRound()
        saverLoader.updateTournament(tournament)
        saverLoader.saveData()

    def addScores(self, saverLoader, view, rapportView, menuView, tournament):
        table4 = [["Tour", "Id ", "Joueur 1", "Joueur 2", "Score"]]
        for match in tournament.roundList[len(tournament.roundList)-1].matchList:
            scores= ' '
            if match.duo[0][1] == None:
                scores = 'Non renseigné'
            else: 
                scores = f"{match.duo[0][1]}/{match.duo[1][1]}"
            table4.append([tournament.roundList[len(tournament.roundList)-1].name, match.id, f"{match.duo[0][0].nrFFE} : {match.duo[0][0].lastName}  {match.duo[0][0].firstName} ({match.duo[0][0].elo})", f"{match.duo[1][0].nrFFE} : {match.duo[1][0].lastName}  {match.duo[1][0].firstName} ({match.duo[1][0].elo})", scores])
        rapportView.printActualRound(table4, tournament)
        choice = menuView.scoresTypeIntegration(tournament)
        return choice

    def printPlayerScores(self, rapportView, tournament):
        table = [['Nom', 'Prénom', 'score', 'Nom de naissance', 'N°FFE', 'Elo']]
        tournament.playerList.sort(key=lambda player: player[0].firstName)
        tournament.playerList.sort(key=lambda player: player[0].lastName)
        tournament.playerList.sort(key=lambda player: player[1], reverse=True)
        for player, score in tournament.playerList:
            table.append([player.lastName, player.firstName, score, player.birthName, player.nrFFE, player.elo])
        rapportView.printPlayerScores(table, tournament)

    def playMatchRandom(self, saverLoader, tournament):
        for match in tournament.roundList[len(tournament.roundList)-1].matchList:
            match.jouerMatch()
            saverLoader.updateTournament(tournament)
            
    def endARound(self, view, saverLoader, tournament):
        validation = True
        for match in tournament.roundList[len(tournament.roundList)-1].matchList:
            if match.duo[0][1] == None:
                validation = False    
        if validation == True :
            tournament.roundList[len(tournament.roundList)-1].endRound()
            tournament.updateScores()
            saverLoader.updateTournament(tournament)
            saverLoader.saveData()
            return True
        else : 
            view.blockvalidation()
            
    def endTournament(self, saverLoader, tournament):
        tournament.setEndDate()
        saverLoader.updateTournament(tournament)
        
    def postScores(self, saverLoader, view, rapportView, tournament):
        table4 = [["Tour", "Id ", "Joueur 1", "Joueur 2", "Score"]]
        nrRoundList= []
        for match in tournament.roundList[len(tournament.roundList)-1].matchList:
            scores= ' '
            nrRoundList.append(match.id)    
            if match.duo[0][1] == None:
                scores = 'Non renseigné'
            else: 
                scores = f"{match.duo[0][1]}/{match.duo[1][1]}"
            table4.append([tournament.roundList[len(tournament.roundList)-1].name, match.id, f"{match.duo[0][0].nrFFE} : {match.duo[0][0].lastName}  {match.duo[0][0].firstName} ({match.duo[0][0].elo})", f"{match.duo[1][0].nrFFE} : {match.duo[1][0].lastName}  {match.duo[1][0].firstName} ({match.duo[1][0].elo})", scores])
        rapportView.printActualRound(table4, tournament)
        idMatch, player1Score = view.scoresIntegration(tournament, nrRoundList)
        for match in tournament.roundList[len(tournament.roundList)-1].matchList:
            if match.id == idMatch: 
                if player1Score == ('P'):
                    match.duo[0][1]=0
                    match.duo[1][1]=1
                if player1Score == ('G'):
                    match.duo[0][1]=1
                    match.duo[1][1]=0
                if player1Score == ('E'):
                    match.duo[0][1]=0.5
                    match.duo[1][1]=0.5
        saverLoader.updateTournament(tournament)