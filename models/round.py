import datetime
from models.match import Match
import random


class Round:
    id = 0

    def __init__(self):
        Round.id += 1
        self.id = Round.id
        self.name = f'Tour {self.id}'
        self.matchList = []
        self.startDate = datetime.datetime.today()
        self.endDate = None

    def to_dict(self):
        if self.endDate is None:
            return {
                "round": {
                    "id": self.id,
                    "name": self.name,
                    "matchList": [match.to_dict() for match in self.matchList],
                    "startDate": self.startDate.isoformat(),
                    "endDate": None,
                    }
                }
        else:
            return {
                "round": {
                    "id": self.id,
                    "name": self.name,
                    "matchList": [match.to_dict() for match in self.matchList],
                    "startDate": self.startDate.isoformat(),
                    "endDate": self.endDate.isoformat(),
                    }
                }

    def addMatch(self, match):
        self.matchList.append(match)

    def endRound(self):
        self.endDate = datetime.datetime.today()
        print(f'round {self.id} est terminé')

    def createMatchList(self, playerlist):
        couples = len(playerlist)/2
        newPlayerList = []
        groups = {}
        for element in playerlist:
            score = element[1]
            if score not in groups:
                groups[score] = []
            groups[score].append(element)
        for group in groups.values():
            print("avant mélange")
            for element in group:
                print(element[0].firstName)
            random.shuffle(group)
            print("après mélange")
            for element in group:
                print(element[0].firstName)
        playerlist = []
        for group in groups.values():
            playerlist.extend(group)
        for x in range(int(couples)):
            if playerlist[0][0].lastOpponent != 'Personne':
                #if playerlist[0][0].lastOpponent in (playerlist[0][0].nrFFE, playerlist[1][0].nrFFE):
                if playerlist[0][0].lastOpponent in (playerlist[0][0].nrFFE,
                                                     playerlist[1][0].nrFFE):
                    if len(playerlist) == 2:
                        newPlayerList.append(playerlist[0])
                        newPlayerList.append(playerlist[1])
                        playerlist.pop(1)
                        playerlist.pop(0)
                    else:
                        newPlayerList.append(playerlist[0])
                        newPlayerList.append(playerlist[2])
                        playerlist.pop(2)
                        playerlist.pop(0)
                else:
                    newPlayerList.append(playerlist[0])
                    newPlayerList.append(playerlist[1])
                    playerlist.pop(1)
                    playerlist.pop(0)
            else:
                newPlayerList.append(playerlist[0])
                newPlayerList.append(playerlist[1])
                playerlist.pop(1)
                playerlist.pop(0)
        for x in range(int(couples)):
            self.matchList.append(Match(newPlayerList[(2*x)][0],
                                        newPlayerList[1+(2*x)][0]))
        for player in newPlayerList:
            playerlist.append(player)
        for match in self.matchList:
            match.duo[0][0].lastOpponent = match.duo[1][0].nrFFE
            match.duo[1][0].lastOpponent = match.duo[0][0].nrFFE

    def printListMatch(self):
        print(f"--- Liste des match du {self.name} ---")
        for match in self.matchList:
            match.__str__()

    def __str__(self):
        print(f"--- Détail du round {self.name} ayant l'id {self.id} ---")
        print(f"--- Date de début : {self.startDate}")
        print(f"--- Date de fin : {self.endDate}")
        self.printListMatch()

    def playRound(self):
        for match in self.matchList:
            match.jouerMatch()
        self.endRound()
