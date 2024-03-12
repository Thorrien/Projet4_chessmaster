import datetime


class Tournament:
    def __init__(self, name, place, nrRound=4):
        self.name = name
        self.place = place
        self.startDate = datetime.datetime.today()
        self.endDate = None
        self.nrRound = nrRound
        self.actualRound = 0
        self.roundList = []
        self.payerList = []
        self.description = f"Tournoi {self.name}"

    def __str__(self):
        return f"Tournoi {self.name} commencé le : {self.startDate}"

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

    def getPayerList(self):
        return self.payerList

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
        self.payerList.append(player)

    def setDescription(self, newDescription):
        self.description = newDescription
