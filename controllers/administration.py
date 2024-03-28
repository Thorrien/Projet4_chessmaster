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

    def modifyMember(self, view, saverLoader):
            while True:
                    #try:
                        nrFFE = view.modifyPlayer1()
                        lastName, firstName, birthName, nrFFE, elo = saverLoader.getPlayerFromJson(nrFFE)
                        element = view.modifyPlayer2(lastName, firstName, birthName, nrFFE, elo)
                        if element != '6':
                            data = view.modifyPlayer4()
                            if element == '1':
                                lastName = data
                            elif element == '2':
                                firstName = data
                            elif element == '3':
                                birthName = data
                            elif element == '4':
                                pass
                            elif element == '5':
                                elo = data
                            player = Player(lastName, firstName)
                            player.birthName = birthName
                            player.nrFFE = nrFFE
                            player.elo = elo
                            print(f"{player.firstName}, {player.lastName}, {player.birthName}, {player.nrFFE}, {player.elo}")
                            saverLoader.updatePlayer(player)
                            break
                        else: 
                            break
                    #except :
                        view.modifyPlayer3()
                        
    def printMember(self, view, saverLoader):
        playerList = saverLoader.loadAllPlayers()
        playerList.sort(key=lambda player: player.firstName)
        playerList.sort(key=lambda player: player.lastName)
        table = [['Nom', 'Prénom', 'Nom de naissance', 'N°FFE', 'Elo']]
        for player in playerList:
            table.append([player.lastName, player.firstName, player.birthName, player.nrFFE, player.elo])
        view.printMember(table)
        
    def printActivity(self, view, saverLoader):
        activityList = saverLoader.getAllActivity()
        activityList.sort(key=lambda activity: activity.date)
        table = [['Date', 'Activity']]
        for activity in activityList:
            table.append([activity.date, activity.type])
        view.activityList(table)
