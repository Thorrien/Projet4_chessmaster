
class MenuManager:
    def __init__(self):
        pass

    def initial(self, view, admin, saverLoader, menuView, rapportView):
        choice=None
        while choice != 9:
            choice = None
            choice = view.menu()
            if choice == 1 :
                choice = view.administration()
                if choice == 1 :
                    admin.addmember(view, saverLoader)
                elif choice == 2 :
                    admin.modifyMember(view, saverLoader)
                elif choice == 3 :
                    admin.printMember(view, saverLoader)
                elif choice == 4 :
                    admin.printActivity(view, saverLoader)
                elif choice == 5 :
                    continue 
            elif choice == 2 :
                choice = view.tournament()
                if choice == 1 :
                    pass
                elif choice == 2 :
                    pass
                elif choice == 3 :
                    pass
                elif choice == 4 :
                    continue 
            elif choice == 3 :
                choice = view.rapports()
                if choice == 1 :
                    admin.printMember(view, saverLoader)
                elif choice == 2 :
                    pass
                elif choice == 3 :
                    pass
                elif choice == 6 :
                    continue 
                
                
        view.quit()