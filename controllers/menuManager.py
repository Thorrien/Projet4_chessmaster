
class MenuManager:
    def __init__(self):
        pass

    def initial(self, view, admin, saverLoader, tournamentManager, menuView, rapportView):
        choice=None
        while choice != 9:
            choice = None
            choice = menuView.menu()
            if choice == 1 :
                choice = menuView.administration()
                if choice == 1 :
                    admin.addmember(view, saverLoader)
                elif choice == 2 :
                    admin.modifyMember(view, saverLoader)
                elif choice == 3 :
                    admin.printMember(view, saverLoader, rapportView)
                elif choice == 4 :
                    admin.printActivity(view, saverLoader, rapportView)
                elif choice == 5 :
                    continue 
            elif choice == 2 :
                choice = menuView.tournament()
                if choice == 1 :
                    tournamentManager.createTournament(view, saverLoader)
                elif choice == 2 :
                    tournamentManager.continueTournament(saverLoader, view, rapportView)
                elif choice == 3 :
                    tournamentManager.printAllTournament(saverLoader, rapportView)
                elif choice == 4 :
                    continue 
            elif choice == 3 :
                choice = menuView.rapports()
                if choice == 1 :
                    admin.printMember(view, saverLoader, rapportView)
                elif choice == 2 :
                    tournamentManager.printAllTournament(saverLoader, rapportView)
                elif choice == 3 :
                    tournamentManager.printspecifictournament(saverLoader, view, rapportView)
                elif choice == 4:
                    tournamentManager.playerListOfASpecificTournament(saverLoader, view, rapportView)    
                elif choice == 5 :
                    tournamentManager.matchListOfASpecificTournament(saverLoader, view, rapportView)
                elif choice == 6 :
                    continue 
                
                
        view.quit()