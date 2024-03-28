
class MenuManager:
    def __init__(self):
        pass

    def initial(self, view, admin, saverLoader):
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
            elif choice == 2 :
                choice = view.tournament()
        view.quit()