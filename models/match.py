

class Match:
    id = 0
    def __init__(self, player1, player2):
        Match.id += 1
        self.id = Match.id
        self.playerList = (player1, player2)
        self.score = None

    def setScore(self, score):
        self.score = score
        