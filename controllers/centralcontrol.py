from models.tournament import *
from controllers.saveload import *
from views.view import View
from time import sleep
from controllers.menuManager import MenuManager
from controllers.administration import Admin

class CentralControl:
    def __init__(self):   
        self.view = View()
        self.menuManager = MenuManager()
        self.saverLoader = SaverLoader()
        self.admin = Admin()
        self.playerList = self.saverLoader.loadAllPlayers()


    def run(self):
        self.view.accueil()
        self.view.loading()
        sleep(2)
        self.importData()
        self.menuManager.initial(self.view, self.admin, self.saverLoader)


    def importData(self):
        self.saverLoader.loadData()
        self.view.data(Tournament.id, Round.id, Match.id, len(self.playerList))