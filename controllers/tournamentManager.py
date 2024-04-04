from models.tournament import Tournament


class TournamentManager:
    def __init__(self):
        pass

    def createTournament(self, view, saverLoader):
        """
        Récupère les informations d'un tournoi venant de la vue et le
        sauvegarde

        Args:
            view: Vue pour  la récupération des données.
            saverLoader: Gestionnaire de sauvegarde et de chargement.

        Returns :
            None

        """
        view.startTournament()
        name, place, description, nrRound = view.createTournament()
        tournament = Tournament(name, place)
        tournament.description = description
        tournament.nrRound = nrRound
        saverLoader.saveTournament(tournament)

    def printAllTournament(self, saverLoader, rapportView):
        """
        Récupère les informations des tournois sauvegardés
        Intègre les données dans un tableau, les envoie à la
        vue et retourne une liste d'id des tournois.

        Args:
            rapportview: Vue pour  l'affichage des tableaux.
            saverLoader: Gestionnaire de sauvegarde et de chargement.

        Returns List :
            Liste des id des tournois

        """
        idList = []
        tournaments = saverLoader.loadAllTournament()
        tournaments.sort(key=lambda tournament: tournament.startDate,
                         reverse=True)
        table = [['Date', 'id', 'Nom du tournoi', 'Etat',
                  'tours', 'Nombre de joueurs']]
        for tournament in tournaments:
            if tournament.endDate:
                etat = 'Terminé'
                idList.append(tournament.id)
            else:
                etat = 'En cours'
                idList.append(tournament.id)
            table.append([tournament.startDate, tournament.id,
                          tournament.name, etat,
                          f'{tournament.actualRound} / {tournament.nrRound}',
                          len(tournament.playerList)])
        rapportView.tournamentsList(table)
        idList.append(tournament.id)
        return idList

    def printActivesTournament(self, saverLoader, rapportView):
        """
        Récupère les informations des tournois sauvegardés
        Trie les tournois pour ne récupérer que les actifs
        Intègre les données dans un tableau, les envoie à la
        vue et retourne une liste d'id des tournois.

        Args:
            rapportview: Vue pour  l'affichage des tableaux.
            saverLoader: Gestionnaire de sauvegarde et de chargement.

        Returns List :
            Liste des id des tournois en cours

        """
        idList = []
        tournaments = saverLoader.loadAllTournament()
        tournaments.sort(key=lambda tournament: tournament.startDate,
                         reverse=True)
        table = [['Date', 'id', 'Nom du tournoi', 'Etat', 'tours',
                  'Nombre de joueurs']]
        for tournament in tournaments:
            if tournament.endDate:
                etat = 'Terminé'
            else:
                etat = 'En cours'
                table.append([
                    tournament.startDate, tournament.id,
                    tournament.name, etat,
                    f'{tournament.actualRound} / {tournament.nrRound}',
                    len(tournament.playerList)])
                idList.append(tournament.id)
        rapportView.tournamentsACList(table)
        return idList

    def continueTournament(self, saverLoader, view, rapportView):
        """
        Récupère l'id du tournoi de la vue et retourne le choix.

        Args:
            view: Vue pour  la récupération des données.
            rapportview: Vue pour  l'affichage des tableaux.
            saverLoader: Gestionnaire de sauvegarde et de chargement.

        Returns List :
            Liste des id des tournois

        """
        idList = self.printActivesTournament(saverLoader, rapportView)
        choice = view.tournamentChoice(idList)
        return choice

    def manageTment(self, saverLoader, view, rapportView,
                    menuView, choice):
        """
        Gère l'affichage des tournois actif en constituant le tableau.
        et l'envoie a la vue.
        Même chose pour la liste des joueurs du tournoi.
        Affiche un menu de gestion du dournoi et
        récupère le choix de l'utilisateur

        Args:
            saverLoader: Gestionnaire de sauvegarde et de chargement.
            view: Vue pour  la récupération des données.
            rapportview: Vue pour  l'affichage des tableaux.
            menueview : Vue pour l'affichage des menus.

        Returns Tournament, choice :
            Tournoi et choix de l'utilisateur

        """
        tournament = saverLoader.loadSpecificTournament(choice)
        table = [['id', 'Nom du tournoi', 'Date', 'tours']]
        table.append([tournament.id, tournament.name,
                      tournament.startDate,
                      f'{tournament.actualRound} / {tournament.nrRound}'])
        table2 = [['Nom', 'Prénom', 'score', 'Nom de naissance',
                   'N°FFE', 'Elo']]
        tournament.playerList.sort(key=lambda player: player[0].firstName)
        tournament.playerList.sort(key=lambda player: player[0].lastName)
        for player in tournament.playerList:
            table2.append([player[0].lastName, player[0].firstName, player[1],
                           player[0].birthName, player[0].nrFFE,
                           player[0].elo])
        rapportView.driveTournament(tournament)
        choice = menuView.choiceDriveTournament(tournament)
        return tournament, choice

    def modifyTournament(self, saverLoader, view, rapportView, tournament):
        """
        Récupère les infos d'un tournoi et propose à
        l'utilisateur d'en modifier une.
        Sauvegarde la modification.

        Args:
            saverLoader: Gestionnaire de sauvegarde et de chargement.
            view: Vue pour  la récupération des données.
            rapportview: Vue pour  l'affichage des tableaux.
            tournament : tournoi a modifier

        Returns :
            None

        """
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
        """
        Affiche la liste des joueurs du club et propose
        d'ajouter un joueur au tournoi.
        Sauvegarde le tournoi avec le joueur.

        Args:
            saverLoader: Gestionnaire de sauvegarde et de chargement.
            view: Vue pour  la récupération des données.
            rapportview: Vue pour  l'affichage des tableaux.
            tournament : tournoi a modifier

        Returns :
            None

        """
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
                table.append([player.nrFFE, player.lastName,
                              player.firstName, player.birthName, player.elo])
            table2 = [['Nom', 'Prénom', 'score', 'Nom de naissance',
                       'N°FFE', 'Elo']]
            if len(tournament.playerList) != 0:
                tournament.playerList.sort(
                    key=lambda player: player[0].firstName)
                tournament.playerList.sort(
                    key=lambda player: player[0].lastName)
                for player in tournament.playerList:
                    FFEList2.append(player[0].nrFFE)
                    table2.append([player[0].lastName, player[0].firstName,
                                   player[1], player[0].birthName,
                                   player[0].nrFFE, player[0].elo])
            nrFFE = None
            nrFFE = rapportView.addPlayer(table, table2, tournament, FFEList)
            if nrFFE != 'Terminé':
                playeradded = saverLoader.getPlayerFromJson(nrFFE)
                if nrFFE in FFEList2:
                    view.addPlayerAlreadyPresent()
                else:
                    tournament.addPayerList(playeradded)
                    saverLoader.updateTournament(tournament)
            else:
                nrFFE = 'Terminé'

    def printspecifictournament(self, saverLoader, view, rapportView):
        """
        Affiche la liste des tournois, demande l'id et
        Affiche les détails d'un tournoi

        Args:
            saverLoader: Gestionnaire de sauvegarde et de chargement.
            view: Vue pour  la récupération des données.
            rapportview: Vue pour  l'affichage des tableaux.

        Returns :
            None

        """
        idList = self.printAllTournament(saverLoader, rapportView)
        choice = view.tournamentChoice(idList)
        tournament = saverLoader.loadSpecificTournament(choice)
        tables = []
        if tournament.endDate:
            etat = 'Terminé'
        else:
            etat = 'En cours'
        table = [['id', 'Nom du tournoi', 'Date', 'tours', 'Etat']]
        table.append([tournament.id, tournament.name,
                      tournament.startDate,
                      f'{tournament.actualRound} / {tournament.nrRound}',
                      etat])
        table2 = [['Nom', 'Prénom', 'score', 'Nom de naissance',
                   'N°FFE', 'Elo']]
        tournament.playerList.sort(key=lambda player: player[0].firstName)
        tournament.playerList.sort(key=lambda player: player[0].lastName)
        for player in tournament.playerList:
            table2.append([player[0].lastName, player[0].firstName, player[1],
                           player[0].birthName, player[0].nrFFE,
                           player[0].elo])
        table3 = [["id", "Nom du Tour", "Date de début", "Nombre de match",
                   "Date de fin"]]
        table4 = [["Tour", "Id du match", "Joueur 1", "Joueur 2", "Score"]]
        for round in tournament.roundList:
            table4 = [["Tour", "Id ", "Date", "Joueur 1", "Joueur 2", "Score"]]
            table3.append([round.id, round.name, round.startDate,
                           len(round.matchList), round.endDate])
            for match in round.matchList:
                table4.append([
                    round.name,
                    match.id,
                    f"{match.duo[0][0].nrFFE} : {match.duo[0][0].lastName}",
                    f"{match.duo[1][0].nrFFE} : {match.duo[1][0].lastName}",
                    f"{match.duo[0][1]}/{match.duo[1][1]}"])
            tables.append(table4)
        rapportView.printTournament(table, table2, table3, tables, tournament)

    def playerListOfASpecificTournament(self, saverLoader, view, rapportView):
        """
        Affiche la liste des tournois, demande l'id et
        Affiche la liste des joueurs d'un tournoi

        Args:
            saverLoader: Gestionnaire de sauvegarde et de chargement.
            view: Vue pour  la récupération des données.
            rapportview: Vue pour  l'affichage des tableaux.

        Returns :
            None

        """
        idList = self.printAllTournament(saverLoader, rapportView)
        choice = view.tournamentChoice(idList)
        tournament = saverLoader.loadSpecificTournament(choice)
        table2 = [['Nom', 'Prénom', 'score', 'Nom de naissance',
                   'N°FFE', 'Elo']]
        tournament.playerList.sort(key=lambda player: player[0].firstName)
        tournament.playerList.sort(key=lambda player: player[0].lastName)
        for player in tournament.playerList:
            table2.append([player[0].lastName, player[0].firstName, player[1],
                           player[0].birthName, player[0].nrFFE,
                           player[0].elo])
        rapportView.printPlayerListTournament(table2, tournament)

    def matchListOfASpecificTournament(self, saverLoader, view, rapportView):
        """
        Affiche la liste des tournois, demande l'id et
        Affiche la liste des matchs d'un tournoi

        Args:
            saverLoader: Gestionnaire de sauvegarde et de chargement.
            view: Vue pour  la récupération des données.
            rapportview: Vue pour  l'affichage des tableaux.

        Returns :
            None

        """
        idList = self.printAllTournament(saverLoader, rapportView)
        choice = view.tournamentChoice(idList)
        tournament = saverLoader.loadSpecificTournament(choice)
        tables = []
        table4 = [["Tour", "Id du match", "Joueur 1", "Joueur 2", "Score"]]
        for round in tournament.roundList:
            table4 = [["Tour", "Id ", "Date", "Joueur 1", "Joueur 2", "Score"]]
            for match in round.matchList:
                table4.append([
                    round.name,
                    match.id,
                    f"{match.duo[0][0].nrFFE} : {match.duo[0][0].lastName}",
                    f"{match.duo[1][0].nrFFE} : {match.duo[1][0].lastName}",
                    f"{match.duo[0][1]}/{match.duo[1][1]}"])
            tables.append(table4)
        rapportView.printMatchListTournament(tables, tournament)

    def runNextTournament(self, saverLoader, tournament):
        """
            Lance un nouveau tour d'un tournoi

        Args:
            saverLoader: Gestionnaire de sauvegarde et de chargement.
            tournament : tournoi

        Returns :
            None

        """
        tournament.createRound()
        saverLoader.updateTournament(tournament)

    def addScores(self, saverLoader, view, rapportView, menuView, tournament):
        """
        Affiche la liste des matchs, demande la méthode d'ajou des scores

        Args:
            saverLoader: Gestionnaire de sauvegarde et de chargement.
            view: Vue pour  la récupération des données.
            rapportview: Vue pour  l'affichage des tableaux.
            menueview: Vue pour afficher un menu
            tournament : tournoi

        Returns :
            None

        """
        table4 = [["Tour", "Id ", "Joueur 1", "Joueur 2", "Score"]]
        for match in tournament.roundList[len(
                tournament.roundList)-1].matchList:
            scores = ' '
            if match.duo[0][1] is None:
                scores = 'Non renseigné'
            else:
                scores = f"{match.duo[0][1]}/{match.duo[1][1]}"
            table4.append([
                tournament.roundList[len(tournament.roundList)-1].name,
                match.id,
                f"{match.duo[0][0].nrFFE} : {match.duo[0][0].lastName}",
                f"{match.duo[1][0].nrFFE} : {match.duo[1][0].lastName}",
                scores])
        rapportView.printActualRound(table4, tournament)
        choice = menuView.scoresTypeIntegration(tournament)
        return choice

    def printPlayerScores(self, rapportView, tournament):
        """
        Affiche la liste des scores d'un tournois

        Args:
            rapportview: Vue pour  l'affichage des tableaux.
            tournament: tournoi

        Returns :
            None

        """
        table = [['Nom', 'Prénom', 'score',
                  'Nom de naissance', 'N°FFE', 'Elo']]
        tournament.playerList.sort(key=lambda player: player[0].firstName)
        tournament.playerList.sort(key=lambda player: player[0].lastName)
        tournament.playerList.sort(key=lambda player: player[1], reverse=True)
        for player, score in tournament.playerList:
            table.append([player.lastName, player.firstName, score,
                          player.birthName, player.nrFFE, player.elo])
        rapportView.printPlayerScores(table, tournament)

    def playMatchRandom(self, saverLoader, tournament):
        """
        Joue les matchs aléatoirement

        Args:
            saverLoader: Gestionnaire de sauvegarde et de chargement.
            tournament : tournoi

        Returns :
            None

        """
        for match in tournament.roundList[len(
                tournament.roundList)-1].matchList:
            match.jouerMatch()
            saverLoader.updateTournament(tournament)

    def endARound(self, view, saverLoader, tournament):
        """
        Termine le dernier tour d'un tournoi.

        Args:
            view: Vue pour  la récupération des données.
            saverLoader: Gestionnaire de sauvegarde et de chargement.
            tournament: Tournoi

        Returns bool:
            True si la démarche est exécutée et sauvegardée

        """
        validation = True
        for match in tournament.roundList[len(
                tournament.roundList)-1].matchList:
            if match.duo[0][1] is None:
                validation = False
        if validation is True:
            tournament.roundList[len(tournament.roundList)-1].endRound()
            tournament.updateScores()
            saverLoader.updateTournament(tournament)
            return True
        else:
            view.blockvalidation()

    def endTmt(self, saverLoader, tournament):
        """
        Termine le tournoi.

        Args:
            saverLoader: Gestionnaire de sauvegarde et de chargement.
            tournament: Tournoi

        Returns :
            None

        """
        tournament.setEndDate()
        saverLoader.updateTournament(tournament)

    def postScores(self, saverLoader, view, rapportView, tournament):
        """
        Demande l'id et le score du joueur 1.
        Puis met a jour le tournoi en appliquant le bon score aux deux joueurs.

        Args:
            saverLoader: Gestionnaire de sauvegarde et de chargement.
            view: Vue pour  la récupération des données.
            rapportview: Vue pour  l'affichage des tableaux.
            tournament : tournoi

        Returns :
            None

        """
        table4 = [["Tour", "Id ", "Joueur 1", "Joueur 2", "Score"]]
        nrRoundList = []
        for match in tournament.roundList[len(
                tournament.roundList)-1].matchList:
            scores = ' '
            nrRoundList.append(match.id)
            if match.duo[0][1] is None:
                scores = 'Non renseigné'
            else:
                scores = f"{match.duo[0][1]}/{match.duo[1][1]}"
            table4.append([
                tournament.roundList[len(tournament.roundList)-1].name,
                match.id,
                f"{match.duo[0][0].nrFFE} : {match.duo[0][0].lastName}",
                f"{match.duo[1][0].nrFFE} : {match.duo[1][0].lastName}",
                scores])
        rapportView.printActualRound(table4, tournament)
        idMatch, player1Score = view.scoresIntegration(tournament, nrRoundList)
        for match in tournament.roundList[len(
                tournament.roundList)-1].matchList:
            if match.id == idMatch:
                if player1Score == ('P'):
                    match.duo[0][1] = 0
                    match.duo[1][1] = 1
                if player1Score == ('G'):
                    match.duo[0][1] = 1
                    match.duo[1][1] = 0
                if player1Score == ('E'):
                    match.duo[0][1] = 0.5
                    match.duo[1][1] = 0.5
        saverLoader.updateTournament(tournament)
