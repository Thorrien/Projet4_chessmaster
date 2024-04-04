from models.player import Player


class Admin:
    def __init__(self):
        pass

    def addmember(self, view, saverLoader):
        """
        Ajoute un nouveau joueur au Json du club.

        Args:
            view: Vue pour  la récupération des données.
            saverLoader: Gestionnaire de sauvegarde et de chargement.

        Returns:
            None

        """
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
        """
        Modifie une caractéristique d'un joueur du club.
        Ensuite enregistre le joueur.

        Args:
            view: Vue pour  la récupération des données.
            saverLoader: Gestionnaire de sauvegarde et de chargement.

        Returns:
            None

        """
        while True:
            try:
                nrFFE = view.modifyPlayer1()
                player = saverLoader.getPlayerFromJson(nrFFE)
                element = view.modifyPlayer2(player)
                if element != '5':
                    data = view.modifyPlayer4()
                    if element == '1':
                        player.lastName = data
                    elif element == '2':
                        player.firstName = data
                    elif element == '3':
                        player.birthName = data
                    elif element == '4':
                        player.elo = data
                    print(
                        f"{player.firstName}, {player.lastName}, "
                        f"{player.birthName}, {player.nrFFE}, {player.elo}"
                    )
                    saverLoader.updatePlayer(player)
                    break
                else:
                    break
            except Exception:
                view.modifyPlayer3()

    def printMember(self, view, saverLoader, rapportView):
        """
        Génère un tableau des joueurs du club.
        Transfère le tableau à la vue adaptée.

        Args:
            view, rapportView: Vue pour  l'affichage des données.
            saverLoader: Gestionnaire de sauvegarde et de chargement.

        Returns:
            None

        """
        playerList = saverLoader.loadAllPlayers()
        playerList.sort(key=lambda player: player.firstName)
        playerList.sort(key=lambda player: player.lastName)
        table = [['Nom', 'Prénom', 'Nom de naissance', 'N°FFE', 'Elo']]
        for player in playerList:
            table.append([player.lastName, player.firstName, player.birthName,
                          player.nrFFE, player.elo])
        rapportView.printMember(table)

    def printActivity(self, view, saverLoader, rapportView):
        """
        Génère un tableau des activité du logiciel (Logs).
        Transfère le tableau à la vue adaptée.

        Args:
            view, rapportView: Vue pour  l'affichage des données.
            saverLoader: Gestionnaire de sauvegarde et de chargement.

        Returns:
            None

        """
        activityList = saverLoader.getAllActivity()
        activityList.sort(key=lambda activity: activity.date)
        table = [['Date', 'Activity']]
        for activity in activityList:
            table.append([activity.date, activity.type])
        rapportView.activityList(table)
