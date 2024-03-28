from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from controllers.saveload import SaverLoader
from controllers.centralcontrol import CentralControl

controlleur = CentralControl()
controlleur.run()






#saverloader = SaverLoader()

#eric = Player('BARILLER','Eric', nrFFE="AA")
#eric2 = Player('BARILLER','Marc', nrFFE="BB")
#eric3 = Player('BARILLER', 'Jean-marie', nrFFE="CC")
#eric4 = Player('BARILLER','Lucie', nrFFE="DD")
#marc = Player('BARILLER', 'Charline', nrFFE="EE")
#marc2 = Player( 'BARILLER','Augustine', nrFFE="FF")
#marc3 = Player( 'BARILLER', 'Achille', nrFFE="GG")
#marc4 = Player( 'BARILLER', 'Abigaëlle', nrFFE="HH")
#marc5 = Player( 'BARILLER', 'Véronique', nrFFE="II")
#marc6 = Player( 'BARILLER', 'Sophie', nrFFE="JJ")
#marc7 = Player( 'BARILLER', 'Cassiopée', nrFFE="KK")
#marc8 = Player('BARILLER', 'Zeus', nrFFE="LL")


#tournoi = Tournament('test2', 'StLeger')
#tournoi.addPayerList(eric)
#tournoi.addPayerList(eric2)
#tournoi.addPayerList(eric3)
#tournoi.addPayerList(eric4)
#tournoi.addPayerList(marc)
#tournoi.addPayerList(marc2)
#tournoi.addPayerList(marc3)
#tournoi.addPayerList(marc4)
#tournoi.addPayerList(marc5)
#tournoi.addPayerList(marc6)
#tournoi.addPayerList(marc7)
#tournoi.addPayerList(marc8)



#for i in range(3):
#    tournoi.createRound()
#    tournoi.roundList[i].playRound()
#    tournoi.roundList[i].__str__()
#    tournoi.updateScores()


#saverloader.saveTournament(tournoi)

#tournoi2 = saverloader.loadTournament(f"data/tournaments/1-test2-Date--2024-03-24.json")

#print(tournoi2.__str__())
#print(tournoi2.getName())
#tournoi2.printPlayerList()
#print(tournoi2.actualRound)
#for round in tournoi2.roundList:
#    round.printListMatch()
    
#saverloader.readTournament()

#for i in range(2):
    
 #   tournoi2.createRound()   
 #   tournoi2.roundList[len(tournoi2.roundList)-1].playRound()
#    tournoi2.roundList[len(tournoi2.roundList)-1].__str__()
#    tournoi2.updateScores()

#saverloader.updateTournament(tournoi2)


#eric.getListMatch()

#tournoi.printPlayerList()

#for (player, score) in tournoi.playerList:
#   savePlayer(player)


#eric = Player('BARILLER', 'Eric', 'BARILLER', nrFFE="AA", elo=15000000)
#updatePlayer(eric)

#recup = loadAllPlayers()

#for player in recup:
#    player.__str__()

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
