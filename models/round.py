import datetime

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