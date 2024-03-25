
class MenuManager:
    def __init__(self):
        pass

    def initial(self, view):
        choice = view.menu()
        if choice == 1 :
            choice = view.administration()
            if choice == 5 :
                choice = self.initial(view)
        elif choice == 2 :
            choice = view.tournament()
