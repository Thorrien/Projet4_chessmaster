import datetime
from models.match import Match

class Round:
    id = 0

    def __init__(self):
        Round.id += 1
        self.id = Round.id
        self.name = f'Round {self.id}'
        self.matchList = []
        self.startDate = datetime.datetime.today()
        self.endDate = None

    def addMatch(self, match):
        self.matchList.append(match)

    def endRound(self):
        self.endDate = datetime.datetime.today()
        print(f'round {self.id} est terminé')

    def createMatchList(self, playerlist):
        couples = len(playerlist)/2
        for x in range(int(couples)):
            self.matchList.append(Match(playerlist[(2*x)][0],playerlist[1+(2*x)][0]))

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
