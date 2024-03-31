import json

class Player:
    def __init__(self, lastName, firstName,
                 birthName="", nrFFE="XXXXXXX", elo=1000, lastOpponent='Personne'):
        self.lastName = lastName
        self.firstName = firstName
        self.birthName = birthName
        self.nrFFE = nrFFE
        self.elo = elo
        self.listMatch = []
        self.lastOpponent= lastOpponent


    def to_dict(self):
        return {
            "player": {
                "nrFFE": self.nrFFE,
                "lastName": self.lastName,
                "firstName": self.firstName,
                "birthName": self.birthName,
                "elo": self.elo,
                "lastOpponent": self.lastOpponent
                #"listMatch": [match.to_dict() for match in self.listMatch]
            }
        }

    def __str__(self):
        print(f"{self.lastName}, {self.firstName}, "
              f"{self.birthName}, {self.nrFFE}, {self.elo}")

    def getlastName(self):
        return self.lastName

    def getfirstName(self):
        return self.lafirstNamestName

    def getbirthName(self):
        return self.birthName

    def getnrFFE(self):
        return self.nrFFE

    def getelo(self):
        return self.elo

    def setlastName(self, newLastName):
        self.lastName = newLastName

    def setfirstName(self, newFirstName):
        self.firstName = newFirstName

    def setbirthName(self, newBirthName):
        self.birthName = newBirthName

    def setnrFFE(self, newNrFFE):
        self.nrFFE = newNrFFE

    def setelo(self, newElo):
        self.elo = newElo


