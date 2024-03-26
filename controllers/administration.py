from models.player import Player

class Admin:
    def __init__(self):
        pass
    
    def addmember(self, view, saverLoader):
        
        lastName, firstName, birthName, nrFFE, elo = view.addmember()
        player = Player(lastName, firstName)
        player.birthName = birthName
        player.nrFFE = nrFFE
        player.elo = elo
        saverLoader.savePlayer(player)