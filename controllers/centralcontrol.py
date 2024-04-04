from models.tournament import Tournament
from models.round import Round
from models.match import Match
from controllers.saveload import SaverLoader
from views.view import View
from views.menuview import MenuView
from views.rapportview import RapportView
from time import sleep
from controllers.menuManager import MenuManager
from controllers.administration import Admin
from models.activity import Activity
from controllers.tournamentManager import TournamentManager


class CentralControl:
    def __init__(self):
        Activity("Start App").saveActivity()
        self.view = View()
        self.menuView = MenuView()
        self.rapportView = RapportView()
        self.menuManager = MenuManager()
        self.saverLoader = SaverLoader()
        self.tournamentManager = TournamentManager()
        self.admin = Admin()
        self.playerList = self.saverLoader.loadAllPlayers()

    def run(self):
        """
        Lance l'application.
        Accueil => Chargement => import des données et le menu.

        Args:
            None

        Returns:
            None

        """
        self.view.accueil()
        self.view.loading()
        sleep(0)
        self.importData()
        self.menuManager.initial(self.view,
                                 self.admin,
                                 self.saverLoader,
                                 self.tournamentManager,
                                 self.menuView,
                                 self.rapportView)

    def importData(self):
        """
        Importe les données du Json Data poir les afficher.

        Args:
            None

        Returns:
            None

        """
        self.saverLoader.loadData()
        self.view.data(Tournament.id, Round.id, Match.id, len(self.playerList))
