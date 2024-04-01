import datetime
import random
from models.round import Round


class Tournament:
    id = 0

    def __init__(self, name, place, nrRound=4):
        Tournament.id += 1
        self.id = Tournament.id
        self.name = name
        self.place = place
        self.startDate = datetime.datetime.today()
        self.endDate = None
        self.nrRound = nrRound
        self.actualRound = 0
        self.roundList = []
        self.playerList = []
        self.description = f"Tournoi {self.name}"

    def __str__(self):
        return f"Tournoi {self.name} commencé le : {self.startDate}"

    def to_dict(self):
        if self.endDate is None:
            return {
                "tournament": {
                    "id": self.id,
                    "name": self.name,
                    "place": self.place,
                    "startDate": self.startDate.isoformat(),
                    "endDate": None,
                    "nrRound": self.nrRound,
                    "actualRound": self.actualRound,
                    "roundList": [round.to_dict() for round in self.roundList],
                    "playerList": [{
                        "player": player.to_dict(),
                        "score": score} for player, score in self.playerList],
                    "description": self.description,
                }
            }
        else:
            return {
                "tournament": {
                    "id": self.id,
                    "name": self.name,
                    "place": self.place,
                    "startDate": self.startDate.isoformat(),
                    "endDate": self.endDate.isoformat(),
                    "nrRound": self.nrRound,
                    "actualRound": self.actualRound,
                    "roundList": [round.to_dict() for round in self.roundList],
                    "playerList": [{
                        "player": player.to_dict(),
                        "score": score} for player, score in self.playerList],
                    "description": self.description,
                }
            }

    def getName(self):
        return self.name

    def getPlace(self):
        return self.place

    def getStartDate(self):
        return self.startDate

    def getEndDate(self):
        return self.endDate

    def getNrRound(self):
        return self.nrRound

    def getActualRound(self):
        return self.actualRound

    def getRoundList(self):
        return self.roundList

    def getPlayerList(self):
        return self.playerList

    def getDescription(self):
        return self.description

    def setName(self, newName):
        self.name = newName

    def setPlace(self, newPlace):
        self.place = newPlace

    def setEndDate(self):
        self.endDate = datetime.datetime.today()

    def setNrRound(self, NewNrRound):
        self.nrRound = NewNrRound

    def setActualRound(self, NewRound):
        self.actualRound = NewRound

    def addRoundList(self, round):
        self.roundList.append(round)

    def addPayerList(self, player):
        score = 0
        self.playerList.append((player, score))

    def setDescription(self, newDescription):
        self.description = newDescription

    def shufflePlayer(self):
        random.shuffle(self.playerList)

    def printPlayerList(self):
        print(f"-----Liste des joueurs du tournoi {self.name}-----")
        for player, score in self.playerList:
            print(f"{player.nrFFE} --- Elo ({player.elo}) -- Score",
                  f" : {score} - {player.firstName}  {player.lastName} ",
                  f" {player.birthName}")

    def createRound(self):
        if self.actualRound != 0:
            self.classifyPlayers(self.playerList)
        else:
            self.shufflePlayer()
        self.roundList.append(Round())
        self.roundList[self.actualRound].createMatchList(self.playerList)
        self.actualRound += 1

    def updateScores(self):
        for match in self.roundList[len(self.roundList)-1].matchList:
            player1, player2 = match.duo[0][0], match.duo[1][0]
            for i, (player, score) in enumerate(self.playerList):
                if player.nrFFE == player1.nrFFE:
                    self.playerList[i] = (player, score + match.duo[0][1])
                elif player.nrFFE == player2.nrFFE:
                    self.playerList[i] = (player, score + match.duo[1][1])

    def classifyPlayers(self, playerlist):
        self.playerList = sorted(self.playerList, key=lambda x: x[1],
                                 reverse=True)
