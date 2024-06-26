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
            "match": {
                "id": self.id,
                "player1": self.duo[0][0].to_dict(),
                "player1score": self.duo[0][1],
                "player2": self.duo[1][0].to_dict(),
                "player2score": self.duo[1][1],
                "date": self.date.isoformat(),
            }
        }

    def jouerMatch(self):
        """
        Joue le match aléatoirement

        Args:
            None

        Returns :
            None

        """
        listeScores = [0, 0.5, 1]
        Player1Score = listeScores[random.randint(0, len(listeScores)-1)]
        if Player1Score == 1:
            self.duo[0][1] = 1
            self.duo[1][1] = 0
        elif Player1Score == 0:
            self.duo[0][1] = 0
            self.duo[1][1] = 1
        elif Player1Score == 0.5:
            self.duo[0][1] = 0.5
            self.duo[1][1] = 0.5

    def getScores(self):
        print(f"Joueur 1 a un score de {self.duo[0][1]}")
        print(f"Joueur 2 a un score de {self.duo[1][1]}")

    def __str__(self):
        nomJoueur1 = f"{self.duo[0][0].firstName} {self.duo[0][0].lastName}"
        nomJoueur2 = f"{self.duo[1][0].firstName} {self.duo[1][0].lastName}"
        print(f" {self.date} | Match {self.id} ",
              f": {nomJoueur1} : {self.duo[0][1]} -vs- {nomJoueur2} :",
              f" {self.duo[1][1]} ")
