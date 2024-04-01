
class MenuManager:
    def __init__(self):
        pass

    def initial(self, view, admin, saverLoader, tournamentManager,
                menuView, rapportView):
        choice = None
        while choice != 9:
            choice = None
            choice = menuView.menu()
            if choice == 1:
                choice = menuView.administration()
                if choice == 1:
                    admin.addmember(view, saverLoader)
                elif choice == 2:
                    admin.modifyMember(view, saverLoader)
                elif choice == 3:
                    admin.printMember(view, saverLoader, rapportView)
                elif choice == 4:
                    admin.printActivity(view, saverLoader, rapportView)
                elif choice == 5:
                    continue
            elif choice == 2:
                choice = menuView.tournament()
                if choice == 1:
                    tournamentManager.createTournament(view, saverLoader)
                elif choice == 2:
                    choice1 = tournamentManager.continueTournament(saverLoader,
                                                                   view,
                                                                   rapportView)
                    manage = True
                    while manage is True:
                        tournament, choice = tournamentManager.manageTment(
                            saverLoader, view, rapportView, menuView, choice1)
                        if choice == 1:
                            tournamentManager.modifyTournament(saverLoader,
                                                               view,
                                                               rapportView,
                                                               tournament)
                        elif choice == 2:
                            if tournament.actualRound != 0:
                                view.blockAddPlayer()
                            else:
                                tournamentManager.addPlayerTournament(
                                    saverLoader, view, rapportView, tournament)
                        elif choice == 3:
                            if tournament.actualRound == 0:
                                if view.confirmation(tournament):
                                    tournamentManager.runNextTournament(
                                        saverLoader, tournament)
                            elif tournament.actualRound == tournament.nrRound:
                                view.maxRound()
                            else:
                                if tournament.roundList[
                                        tournament.actualRound-1
                                        ].endDate is not None:
                                    tournamentManager.runNextTournament(
                                        saverLoader,
                                        tournament
                                    )
                                else:
                                    view.actualRoundNotFinished()
                        elif choice == 4:
                            if (tournament.actualRound == 0 or
                                    tournament.roundList[
                                        tournament.actualRound-1
                                    ].endDate is not None):
                                view.blockscores()
                            else:
                                scores = True
                                while scores is True:
                                    choice = tournamentManager.addScores(
                                        saverLoader, view, rapportView,
                                        menuView, tournament)
                                    if choice == 1:
                                        tournamentManager.postScores(
                                            saverLoader, view,
                                            rapportView, tournament)
                                    elif choice == 2:
                                        save = tournamentManager.endARound(
                                            view, saverLoader, tournament)
                                        if save is True:
                                            if (tournament.actualRound ==
                                                    tournament.nrRound):
                                                tournamentManager.endTmt(
                                                    saverLoader, tournament)
                                            scores = False
                                    elif choice == 3:
                                        tournamentManager.playMatchRandom(
                                            saverLoader, tournament)
                                    elif choice == 4:
                                        scores = False
                                    elif choice == 9:
                                        scores = False
                                        manage = False
                        elif choice == 5:
                            tournamentManager.printPlayerScores(rapportView,
                                                                tournament)
                        elif choice == 6:
                            manage = False
                        elif choice == 9:
                            manage = False
                elif choice == 3:
                    tournamentManager.printAllTournament(saverLoader,
                                                         rapportView)
                elif choice == 4:
                    continue
            elif choice == 3:
                choice = menuView.rapports()
                if choice == 1:
                    admin.printMember(view, saverLoader, rapportView)
                elif choice == 2:
                    tournamentManager.printAllTournament(saverLoader,
                                                         rapportView)
                elif choice == 3:
                    tournamentManager.printspecifictournament(saverLoader,
                                                              view,
                                                              rapportView)
                elif choice == 4:
                    tournamentManager.playerListOfASpecificTournament(
                        saverLoader, view, rapportView)
                elif choice == 5:
                    tournamentManager.matchListOfASpecificTournament(
                        saverLoader, view, rapportView)
                elif choice == 6:
                    continue
        view.quit()
