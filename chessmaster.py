from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match




eric = Player('Eric', 'BARILLER')
eric2 = Player('Marc', 'BARILLER')
eric3 = Player('Jean-marie', 'BARILLER')
eric4 = Player('Lucie', 'BARILLER')
marc = Player('Charline', 'BARILLER')
marc2 = Player('Augustine', 'BARILLER')
marc3 = Player('Achille', 'BARILLER')
marc4 = Player('Abigaëlle', 'BARILLER')
marc5 = Player('Véronique', 'BARILLER')
marc6 = Player('Sophie', 'BARILLER')
marc7 = Player('Cassiopée', 'BARILLER')
marc8 = Player('Zeus', 'BARILLER')

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

tournoi.printPlayerList()

for i in range(10):
    tournoi.createRound()
    tournoi.roundList[i].playRound()
    tournoi.roundList[i].__str__()
    tournoi.updateScores()
    tournoi.printPlayerList()
    tournoi.shufflePlayer()

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
