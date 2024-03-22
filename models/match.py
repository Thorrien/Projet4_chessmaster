import random
import datetime

class Match:
    id = 0
    def __init__(self, player1, player2):
        Match.id += 1
        self.id = Match.id
        self.duo = ([player1, None], [player2, None])
        self.date = datetime.datetime.today()
        
    def to_dict(self):
        return {
            "id": self.id,
            "player1": {
                "lastName": self.duo[0][0].lastName,
                "firstName": self.duo[0][0].firstName,
                "birthName": self.duo[0][0].birthName,
                "nrFFE": self.duo[0][0].nrFFE,
                "elo": self.duo[0][0].elo,
                "score": self.duo[0][1]
            },
            "player2": {
                "lastName": self.duo[1][0].lastName,
                "firstName": self.duo[1][0].firstName,
                "birthName": self.duo[1][0].birthName,
                "nrFFE": self.duo[1][0].nrFFE,
                "elo": self.duo[1][0].elo,
                "score": self.duo[1][1]
            },
            "date": self.date.isoformat(),
        }
        
        
        
        
    def jouerMatch(self):
        listeScores = [0, 0.5, 1]
        Player1Score = listeScores[random.randint(0, len(listeScores)-1)]
        if Player1Score == 1:
            #print(f"{self.duo[0][0].firstName} {self.duo[0][0].lastName} gagne le match")
            self.duo[0][1]=1
            self.duo[1][1]=0
        elif Player1Score == 0:
            #print(f"{self.duo[1][0].firstName} {self.duo[1][0].lastName} gagne le match")
            self.duo[0][1]=0
            self.duo[1][1]=1
        elif Player1Score == 0.5:
            #print("Egalité")
            self.duo[0][1]=0.5
            self.duo[1][1]=0.5
        self.duo[0][0].listMatch.append(self)
        self.duo[1][0].listMatch.append(self)
            
    def getScores(self):
        print(f"Joueur 1 a un score de {self.duo[0][1]}")
        print(f"Joueur 2 a un score de {self.duo[1][1]}")
        
    def __str__(self):
        nomJoueur1 = f"{self.duo[0][0].firstName} {self.duo[0][0].lastName}"
        nomJoueur2 = f"{self.duo[1][0].firstName} {self.duo[1][0].lastName}"
        print(f" {self.date} | Match {self.id} : {nomJoueur1} : {self.duo[0][1]} -vs- {nomJoueur2} : {self.duo[1][1]} ")
