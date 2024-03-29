from tabulate import tabulate


class RapportView:
    def __init__(self):
        pass
    
    def printMember(self, table):
        print('\n\n--------------------------------------------------------------------')
        print("------------------Liste des joueurs du club-------------------------")
        print('--------------------------------------------------------------------')
        print(tabulate(table, headers="firstrow"))

    def activityList(self, table):
        print('\n\n--------------------------------------------------------------------')
        print("------------------Liste des joueurs du club-------------------------")
        print('--------------------------------------------------------------------')
        print(tabulate(table, headers="firstrow"))

    def tournamentsList(self, table):
        print('\n\n--------------------------------------------------------------------')
        print("-------------------Historique des tournois--------------------------")
        print('--------------------------------------------------------------------')
        print(tabulate(table, headers="firstrow"))
        
    def printTournament(self, table, table2, table3, tables, tournament):
        choice = None
        while choice not in ['Non']:
            print('\n\n--------------------------------------------------------------------')
            print("-------------------Informations du tournoi--------------------------\n")
            print(tabulate(table, headers="firstrow"))
            while choice not in ['Oui', 'Non']:
                choice = input('\n\nAfficher la liste des joueurs (Oui/Non) : ')
            print(f"\n          Liste des joueurs du tournoi : {tournament.name}          \n")
            print(tabulate(table2, headers="firstrow"))
            choice = None
            while choice not in ['Oui', 'Non']:
                choice = input('\n\nAfficher la liste des Rounds (Oui/Non) : ')
            print(f"\n          Liste des tours du tournoi : {tournament.name}          \n")
            print(tabulate(table3, headers="firstrow"))
            choice = None
            while choice not in ['Oui', 'Non']:
                choice = input('\n\nAfficher la liste des Matchs par Rounds (Oui/Non) : ')
                for table in tables:
                    print("\n\n")
                    print(tabulate(table, headers="firstrow"))
            choice = 'Non'
            
    def printPlayerListTournament(self, table2, tournament):
        print('\n\n--------------------------------------------------------------------')
        print(f"\n          Liste des joueurs du tournoi : {tournament.name}          \n")
        print(tabulate(table2, headers="firstrow"))
            
    def printMatchListTournament(self, tables, tournament):
        print('\n\n--------------------------------------------------------------------')
        print(f"      Liste des matchs par tours du tournoi {tournament.name}\n")
        for table in tables:
            print("\n\n")
            print(tabulate(table, headers="firstrow"))