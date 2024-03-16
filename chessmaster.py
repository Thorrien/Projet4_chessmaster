from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match




eric = Player('BARILLER','Eric')
eric2 = Player('BARILLER','Marc')
eric3 = Player('BARILLER', 'Jean-marie')
eric4 = Player('BARILLER','Lucie')
marc = Player('BARILLER', 'Charline')
marc2 = Player( 'BARILLER','Augustine')
marc3 = Player( 'BARILLER', 'Achille')
marc4 = Player( 'BARILLER', 'Abigaëlle')
marc5 = Player( 'BARILLER', 'Véronique')
marc6 = Player( 'BARILLER', 'Sophie')
marc7 = Player( 'BARILLER', 'Cassiopée')
marc8 = Player('BARILLER', 'Zeus')

tournoi = Tournament('Noël BARILLER', 'Sablé')
tournoi.addPayerList(eric)
tournoi.addPayerList(eric2)
tournoi.addPayerList(eric3)
tournoi.addPayerList(eric4)
tournoi.addPayerList(marc)
tournoi.addPayerList(marc2)
tournoi.addPayerList(marc3)
tournoi.addPayerList(marc4)
tournoi.addPayerList(marc5)
tournoi.addPayerList(marc6)
tournoi.addPayerList(marc7)
tournoi.addPayerList(marc8)



for i in range(10):
    tournoi.createRound()
    tournoi.roundList[i].playRound()
    tournoi.roundList[i].__str__()
    tournoi.updateScores()


eric.getListMatch()

tournoi.printPlayerList()
#
# 
# 
# 
#round2 = Round()
#round2.createMatchList(tournoi.playerList)
#round2.__str__()
#tournoi.printPlayerList()
#tournoi.shufflePlayer()
#tournoi.printPlayerList()
