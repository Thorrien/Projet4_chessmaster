from controllers.centralcontrol import CentralControl

def main():
    controller = CentralControl()
    controller.run()

if __name__ == "__main__":
    main()



#saverloader = SaverLoader()
#tournamentManager = TournamentManager()#

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
#2


#tournoi = Tournament('Test 3', 'StLeger')
#tournoi.addPayerList(eric)#
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



#for i in range(5):
#    tournoi.createRound()
#    tournoi.printPlayerList()
#    tournoi.roundList[i].playRound()
#    tournoi.roundList[i].__str__()
#    tournoi.updateScores()

#for player, score in tournoi.playerList:
#    saverloader.updatePlayer(player)
#saverloader.saveTournament(tournoi)

#tournoi2 = saverloader.loadSpecificTournament('1')

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
#    tournoi2.roundList[len(tournoi2.roundList)-1].__str__()1

#    tournoi2.updateScores()
#tournoi2.setEndDate()
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
