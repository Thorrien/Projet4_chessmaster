from models.player import Player
from models.round import Round
from models.match import Match
from models.activity import Activity
from models.tournament import Tournament
import json
import os
import datetime


class SaverLoader:

    def __init__(self):
        pass

    def saveData(self):
        """
        Sauvegarde dans le Json les datas de l'application

        Args:
            None

        Returns:
            None

        """
        data = {
                "data": {
                    "tournamentId": Tournament.id,
                    "roundId": Round.id,
                    "matchId": Match.id,
                    }
                }
        file_path = "data/data/data.json"
        with open(file_path, 'w') as file:
            json.dump(data, file)

    def loadData(self):
        """
        Charge les données de l'application.

        Args:
            None

        Returns:
            None

        """
        with open("data/data/data.json", 'r') as file:
            datas = json.load(file)
            data = datas.get("data")
            Tournament.id = data.get("tournamentId")
            Round.id = data.get("roundId")
            Match.id = data.get("matchId")
            Activity("Load data").saveActivity()

    def savePlayer(self, player):
        """
        Sauvegarde dans le Json les donnée d'un joueur

        Args:
            Player

        Returns:
            None

        """
        try:
            with open("data/players/playerList.json", 'r') as mon_fichier:
                players_data = json.load(mon_fichier)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            players_data = []
# Vérification que le joueur est déjà présent dans le Json, si oui update
        player_dict = player.to_dict()
        player_exists = False
        for existing_player in players_data:
            if existing_player["player"][
                    "nrFFE"] == player_dict["player"]["nrFFE"]:
                self.updatePlayer(existing_player)
                player_exists = True
                break
#                                                           , si non ajout
        if not player_exists:
            players_data.append(player_dict)
            Activity("Add Player to club list").saveActivity()

        with open("data/players/playerList.json", 'w') as mon_fichier:
            json.dump(players_data, mon_fichier)

    def cheakPlayer(self, player):
        """
        Controle si le Joueur est présent dans le Json

        Args:
            Player

        Returns Bool:
            True si le joueur est présent.

        """
        try:
            with open("data/players/playerList.json", 'r') as mon_fichier:
                players_data = json.load(mon_fichier)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            players_data = []
        Activity("Cheak Player").saveActivity()
        player_dict = player.to_dict()
        for existing_player in players_data:
            if existing_player["player"][
                    "nrFFE"] == player_dict["player"]["nrFFE"]:
                return True

    def updatePlayer(self, player):
        """
        Update le Joueur dans le JSon

        Args:
            Player

        Returns :
            None

        """
        with open("data/players/playerList.json", 'r') as file:
            players_data = json.load(file)

        for player_data in players_data:
            if player_data["player"]["nrFFE"] == player.nrFFE:
                player_data["player"]["lastName"] = player.lastName
                player_data["player"]["firstName"] = player.firstName
                player_data["player"]["birthName"] = player.birthName
                player_data["player"]["elo"] = player.elo
                player_data["player"]["lastOpponent"] = player.lastOpponent
                break

        with open("data/players/playerList.json", 'w') as file:
            json.dump(players_data, file)
        Activity("Update Player").saveActivity()

    def loadAllPlayers(self):
        """
        Récupère tous les joueurs du Json

        Args:
            None

        Returns List:
            Liste des joueurs.

        """
        listOfPlayers = []
        with open("data/players/playerList.json", 'r') as file:
            players_data = json.load(file)
            Activity("Load all Player").saveActivity()
            for player_data in players_data:
                player = self.createPlayerFromJson(player_data)
                listOfPlayers.append(player)
            return listOfPlayers

    def getPlayerFromJson(self, nrFFE):
        """
        Cherche un numero FFE et retourne le joueur du Json

        Args:
            Numéro FFE du joueur

        Returns Player:
            Joueur.

        """
        with open("data/players/playerList.json", 'r') as file:
            players_data = json.load(file)
        for player_data in players_data:
            if player_data["player"]["nrFFE"] == nrFFE:
                lastName = player_data["player"]["lastName"]
                firstName = player_data["player"]["firstName"]
                birthName = player_data["player"]["birthName"]
                elo = player_data["player"]["elo"]
                lastOpponent = player_data["player"]["lastOpponent"]
                break
        Activity("Get specific Player").saveActivity()
        return Player(lastName, firstName, birthName, nrFFE, elo, lastOpponent)

    def createPlayerFromJson(self, data):
        """
        Créée un joueur à partir d'une data .json

        Args:
            Data d'un joueur au format Json

        Returns Player:
            Joueur.

        """
        player_info = data.get("player")
        lastName = player_info.get("lastName")
        firstName = player_info.get("firstName")
        birthName = player_info.get("birthName", "")
        nrFFE = player_info.get("nrFFE")
        elo = player_info.get("elo")
        lastOpponent = player_info.get("lastOpponent")
        return Player(lastName, firstName, birthName, nrFFE, elo, lastOpponent)

    def createRoundFromJson(self, data):
        """
        Créée un round à partir d'une data .json

        Args:
            Data d'un joueur au format Json

        Returns Round:
            Tour.

        """
        round_info = data.get("round")
        id = round_info.get("id")
        name = round_info.get("name")
        matchList = [(self.createMatchFromJson(
            match_data)) for match_data in round_info['matchList']]
        startDate = datetime.datetime.strptime(round_info.get("startDate"),
                                               "%Y-%m-%dT%H:%M:%S.%f")
        if round_info.get("endDate") is not None:
            endDate = datetime.datetime.strptime(round_info.get("endDate"),
                                                 "%Y-%m-%dT%H:%M:%S.%f")
        else:
            endDate = None
        round = Round()
        round.id = id
        Round.id -= 1
        round.name = name
        round.matchList = matchList
        round.startDate = startDate
        round.endDate = endDate
        return round

    def createMatchFromJson(self, data):
        """
        Créée un match à partir d'une data .json

        Args:
            Data d'un match au format Json

        Returns Match:
            Joueur.

        """
        match_info = data.get("match")
        id = match_info.get("id")
        date = datetime.datetime.strptime(match_info.get("date"),
                                          "%Y-%m-%dT%H:%M:%S.%f")
        player1_data = match_info.get("player1")
        player2_data = match_info.get("player2")
        player1 = self.createPlayerFromJson(player1_data)
        player2 = self.createPlayerFromJson(player2_data)
        duo = ([player1, match_info["player1score"]],
               [player2, match_info["player2score"]])
        match = Match(player1, player2)
        match.id = id
        Match.id -= 1
        match.date = date
        match.duo = duo
        return match

    def saveTournament(self, tournament):
        """
        Enregistre un tournoi dans un fichier Json adapté

        Args:
            tournoi

        Returns :
            None.

        """
        date = tournament.startDate.isoformat().split("T")
        file_path = f"data/tournaments/{
            tournament.id}-{tournament.name}-Date--{date[0]}.json"
        tournamentData = tournament.to_dict()
        Activity("Save Tournament").saveActivity()
        with open(file_path, 'w') as file:
            json.dump(tournamentData, file)
        self.saveData()

    def updateTournament(self, tournament):
        """
        Met à jour un tournoi dans son fichier Json

        Args:
            tournoi

        Returns :
            None.

        """
        files_path = "data/tournaments"
        Activity("Update Tournament").saveActivity()
        for file_name in os.listdir(files_path):
            if file_name.startswith(f'{tournament.id}-'):
                file_path = os.path.join(files_path, file_name)
                tournamentData = tournament.to_dict()
                with open(file_path, 'w') as file:
                    json.dump(tournamentData, file)
        self.saveData()

    def readTournament(self):
        """
        Récupère la liste documents dans le dossier tournaments
        et retourne les informations.

        Args:
            None

        Returns List:
            Une liste d'informations. pour chaque document :
            (Nom du fichier, Chemin d'accès, date)

        """
        tournaments = []
        files_path = "data/tournaments"
        for file_name in os.listdir(files_path):
            file_path = os.path.join(files_path, file_name)
            date = file_name[-15:][:10]
            if os.path.isfile(file_path):
                tournaments.append((file_name, file_path, date))
        Activity("Read Tournament").saveActivity()
        return tournaments

    def loadAllTournament(self):
        """
        Charge tous les tournois des fichiers des tournois

        Args:
            None

        Returns List :
            Liste des tournois

        """
        tournaments = []
        files_path = "data/tournaments"
        for file_name in os.listdir(files_path):
            file_path = os.path.join(files_path, file_name)
            if os.path.isfile(file_path):
                tournaments.append(self.loadTournament(file_path))
        Activity("Read Tournament").saveActivity()
        return tournaments

    def loadTournament(self, files_path):
        """
        Récupère les informations d'un Json d'un tournoi et le
        retourne en instance tournoi

        Args:
            Lien d'accès du document

        Returns Tournament :
            Un tournoi

        """
        with open(files_path, 'r') as file:
            tournament_data = json.load(file)
            tournament_info = tournament_data.get("tournament")
            Activity("Load Tournament").saveActivity()
            id = tournament_info.get("id")
            name = tournament_info.get("name")
            place = tournament_info.get("place")
            startDate = datetime.datetime.strptime(
                tournament_info.get("startDate"), "%Y-%m-%dT%H:%M:%S.%f")
            if tournament_info.get("endDate") is not None:
                endDate = datetime.datetime.strptime(
                    tournament_info.get("endDate"), "%Y-%m-%dT%H:%M:%S.%f")
            else:
                endDate = None
            nrRound = tournament_info.get("nrRound")
            actualRound = tournament_info.get("actualRound")
            roundList = [self.createRoundFromJson(
                round_data) for round_data in tournament_info['roundList']]
            playerList = [(self.createPlayerFromJson(
                player_data["player"]), player_data[
                    "score"]) for player_data in tournament_info['playerList']]
            description = tournament_info.get("description")
            tournament = Tournament(name, place, nrRound)
            tournament.id = id
            Tournament.id -= 1
            tournament.startDate = startDate
            tournament.endDate = endDate
            tournament.actualRound = actualRound
            tournament.description = description
            tournament.playerList = playerList
            tournament.roundList = roundList
            return tournament

    def getAllActivity(self):
        """
        Récupère les informations du Json activity

        Args:
            None

        Returns List :
            Une liste d'activité

        """
        listOfActivity = []
        with open("data/data/activity.json", 'r') as file:
            activities_data = json.load(file)
            for activity_data in activities_data:
                activity = self.createActivityFromJson(activity_data)
                listOfActivity.append(activity)
            return listOfActivity

    def createActivityFromJson(self, data):
        """
        Récupère les informations du Json activity et les
        retournent en instance activity

        Args:
            Lien d'accès du document

        Returns Tournament :
            Un tournoi

        """
        activity_info = data.get("activity")
        date = datetime.datetime.strptime(activity_info.get("date"),
                                          "%Y-%m-%dT%H:%M:%S.%f")
        type = activity_info.get("type")
        activity = Activity(type)
        activity.date = date
        return activity

    def loadSpecificTournament(self, id):
        """
        Récupère les informations d'un Json d'un tournoi et le
        retourne en instance tournoi

        Args:
            Id d'un tournoi

        Returns Tournament :
            Un tournoi

        """
        files_path = "data/tournaments"
        for file_name in os.listdir(files_path):
            if file_name.startswith(str(id)):
                file_path_doc = os.path.join(files_path, file_name)
        with open(file_path_doc, 'r') as file:
            tournament_data = json.load(file)
            tournament_info = tournament_data.get("tournament")
            Activity("Load Tournament").saveActivity()
            id = tournament_info.get("id")
            name = tournament_info.get("name")
            place = tournament_info.get("place")
            startDate = datetime.datetime.strptime(
                tournament_info.get("startDate"), "%Y-%m-%dT%H:%M:%S.%f")
            if tournament_info.get("endDate") is not None:
                endDate = datetime.datetime.strptime(
                    tournament_info.get("endDate"), "%Y-%m-%dT%H:%M:%S.%f")
            else:
                endDate = None
            nrRound = tournament_info.get("nrRound")
            actualRound = tournament_info.get("actualRound")
            roundList = [self.createRoundFromJson(
                round_data) for round_data in tournament_info['roundList']]
            playerList = [(self.createPlayerFromJson(
                player_data["player"]),
                player_data["score"]) for player_data in tournament_info[
                    'playerList']]
            description = tournament_info.get("description")
            tournament = Tournament(name, place, nrRound)
            tournament.id = id
            Tournament.id -= 1
            tournament.startDate = startDate
            tournament.endDate = endDate
            tournament.actualRound = actualRound
            tournament.description = description
            tournament.playerList = playerList
            tournament.roundList = roundList
            return tournament
