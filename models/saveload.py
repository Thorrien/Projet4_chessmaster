from models.player import Player
from models.round import Round
from models.match import Match
from models.tournament import Tournament
import json
import os
import datetime


class SaverLoader:

    def __init__(self):
        pass

    def saveData(self):
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
        with open("data/data/data.json", 'r') as file:
            datas = json.load(file)
            data = datas.get("data")
            Tournament.id = data.get("tournamentId")
            Round.id = data.get("roundId")
            Match.id = data.get("matchId")

    def savePlayer(self, player):
        try:
            with open("data/players/playerList.json", 'r') as mon_fichier:
                players_data = json.load(mon_fichier)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            players_data = []

        player_dict = player.to_dict()
        player_exists = False
        for existing_player in players_data:
            if (existing_player["player"]["nrFFE"] ==
                    player_dict["player"]["nrFFE"]):
                self.updatePlayer(existing_player)
                player_exists = True
                break
        if not player_exists:
            players_data.append(player_dict)
        with open("data/players/playerList.json", 'w') as mon_fichier:
            json.dump(players_data, mon_fichier)

    def updatePlayer(self, player):
        with open("data/players/playerList.json", 'r') as file:
            players_data = json.load(file)

        for player_data in players_data:
            if player_data["player"]["nrFFE"] == player.nrFFE:
                player_data["player"]["lastName"] = player.lastName
                player_data["player"]["firstName"] = player.firstName
                player_data["player"]["birthName"] = player.birthName
                player_data["player"]["elo"] = player.elo
                break

        with open("data/players/playerList.json", 'w') as file:
            json.dump(players_data, file)

    def loadAllPlayers(self):
        listOfPlayers = []
        with open("data/players/playerList.json", 'r') as file:
            players_data = json.load(file)

            for player_data in players_data:
                player = self.createPlayerFromJson(player_data)
                listOfPlayers.append(player)
            return listOfPlayers

    def createPlayerFromJson(self, data):
        player_info = data.get("player")
        lastName = player_info.get("lastName")
        firstName = player_info.get("firstName")
        birthName = player_info.get("birthName", "")
        nrFFE = player_info.get("nrFFE")
        elo = player_info.get("elo")
        return Player(lastName, firstName, birthName, nrFFE, elo)

    def createRoundFromJson(self, data):
        round_info = data.get("round")
        id = round_info.get("id")
        name = round_info.get("name")
        matchList = [
            (self.createMatchFromJson(match_data))
            for match_data in round_info['matchList']
        ]
        startDate = datetime.datetime.strptime(round_info.get("startDate"),
                                               "%Y-%m-%dT%H:%M:%S.%f")
        if round_info.get("endDate") is not None:
            endDate = datetime.datetime.strptime(round_info.get("endDate"),
                                                 "%Y-%m-%dT%H:%M:%S.%f")
        else:
            endDate = None
        round = Round()
        round.id = id
        round.name = name
        round.matchList = matchList
        round.startDate = startDate
        round.endDate = endDate
        return round

    def createMatchFromJson(self, data):
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
        match.date = date
        match.duo = duo
        return match

    def saveTournament(self, tournament):
        date = tournament.startDate.isoformat().split("T")
        file_path = (
            f"data/tournaments/{tournament.id}-{tournament.name}-"
            f"Date--{date[0]}.json"
        )
        tournamentData = tournament.to_dict()
        with open(file_path, 'w') as file:
            json.dump(tournamentData, file)

    def updateTournament(self, tournament):
        files_path = "data/tournaments"
        for file_name in os.listdir(files_path):
            if file_name.startswith(f'{tournament.id}-{tournament.name}-Date'):
                file_path = os.path.join(files_path, file_name)
                tournamentData = tournament.to_dict()
                with open(file_path, 'w') as file:
                    json.dump(tournamentData, file)

    def readTournament(self):
        tournaments = []
        files_path = "data/tournaments"
        for file_name in os.listdir(files_path):
            file_path = os.path.join(files_path, file_name)
            date = file_name[-15:][:10]
            if os.path.isfile(file_path):
                tournaments.append((file_name, file_path, date))
        return tournaments

    def loadTournament(self, files_path):
        with open(files_path, 'r') as file:
            tournament_data = json.load(file)
            tournament_info = tournament_data.get("tournament")
            id = tournament_info.get("id")
            name = tournament_info.get("name")
            place = tournament_info.get("place")
            startDate = datetime.datetime.strptime(
                tournament_info.get("startDate"),
                "%Y-%m-%dT%H:%M:%S.%f"
            )
            if tournament_info.get("endDate") is not None:
                endDate = datetime.datetime.strptime(
                    tournament_info.get("endDate"),
                    "%Y-%m-%dT%H:%M:%S.%f"
                )
            else:
                endDate = None
            nrRound = tournament_info.get("nrRound")
            actualRound = tournament_info.get("actualRound")
            roundList = [
                self.createRoundFromJson(round_data)
                for round_data in tournament_info['roundList']
            ]
            playerList = [
                (
                    self.createPlayerFromJson(player_data["player"]),
                    player_data["score"]
                )
                for player_data in tournament_info['playerList']
            ]
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
