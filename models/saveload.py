from models.player import Player
from models.match import Match
from models.tournament import Tournament
import json
import os
import datetime


class SaverLoader :
    
    def __init__(self):
        pass
    

    def savePlayer(self, player):
        try:
            with open("data/players/playerList.json", 'r') as mon_fichier:
                players_data = json.load(mon_fichier)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            players_data = []

        player_dict = player.to_dict()
        player_exists = False
        for existing_player in players_data:
            if existing_player["player"]["nrFFE"] == player_dict["player"]["nrFFE"]:
                print(f'update du joueur {existing_player["player"]["nrFFE"]}')
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

    def createPlayerFromJson(self,data):
        player_info = data.get("player")
        lastName = player_info.get("lastName")
        firstName = player_info.get("firstName")
        birthName = player_info.get("birthName", "")
        nrFFE = player_info.get("nrFFE")
        elo = player_info.get("elo")
        return Player(lastName, firstName, birthName, nrFFE, elo)


    def saveTournament(self, tournament):
        date = tournament.startDate.isoformat().split("T")
        file_path = f"data/tournaments/{tournament.id}-{tournament.name}-Date--{date[0]}.json"
        tournamentData = tournament.to_dict()
        with open(file_path, 'w') as file:
            json.dump(tournamentData, file)
        print("Fichier JSON créé avec succès.")

    
    def updateTournament(self, tournament):
        pass

    def readTournament(self):
        tournaments = []
        files_path = f"data/tournaments"
        for file_name in os.listdir(files_path):
            file_path = os.path.join(files_path, file_name)
            date = file_name[-15:][:10]
            if os.path.isfile(file_path):  
                tournaments.append((file_name, file_path, date))
        print(tournaments)
        return tournaments
 

    def loadTournament(self, files_path):
        with open(files_path, 'r') as file:
            tournament_data = json.load(file)
            tournament_info = tournament_data.get("tournament")
        
            id = tournament_info.get("id")
            name = tournament_info.get("name")
            place = tournament_info.get("place")
            startDate = datetime.datetime.strptime(tournament_info.get("startDate"), "%Y-%m-%dT%H:%M:%S.%f")
            if tournament_info.get("endDate") != None:
                endDate =  datetime.datetime.strptime(tournament_info.get("endDate"), "%Y-%m-%dT%H:%M:%S.%f")
            else:
                endDate = None
            nrRound = tournament_info.get("nrRound")
            actualRound = tournament_info.get("actualRound")
            #self.roundList = t
            playerList = [(self.createPlayerFromJson(player_data["player"]), player_data["score"]) for player_data in tournament_info['playerList']]
            description = tournament_info.get("description")
            
            tournament = Tournament(name, place, nrRound)
            tournament.id = id
            Tournament.id -= 1
            tournament.startDate = startDate
            tournament.endDate = endDate
            tournament.actualRound = actualRound
            tournament.description = description
            tournament.playerList = playerList
            
            return tournament

       
                    #"roundList": [round.to_dict() for round in self.roundList],
                    #"playerList": [{"player": player.to_dict(), "score": score} for player, score in self.playerList],

