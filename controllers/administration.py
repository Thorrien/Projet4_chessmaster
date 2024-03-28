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
        if saverLoader.cheakPlayer(player):
            if view.modifyConf():
                saverLoader.updatePlayer(player)
        else:
            saverLoader.savePlayer(player)

    def modifyMenber(self, view, saverLoader):
        pass