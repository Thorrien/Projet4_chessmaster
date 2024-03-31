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
            if choice == 'Oui':
                print(f"\n          Liste des joueurs du tournoi : {tournament.name}          \n")
                print(tabulate(table2, headers="firstrow"))
            choice = None
            while choice not in ['Oui', 'Non']:
                choice = input('\n\nAfficher la liste des Rounds (Oui/Non) : ')
            if choice == 'Oui':
                print(f"\n          Liste des tours du tournoi : {tournament.name}          \n")
                print(tabulate(table3, headers="firstrow"))
            choice = None
            while choice not in ['Oui', 'Non']:
                choice = input('\n\nAfficher la liste des Matchs par Rounds (Oui/Non) : ')
            if choice == 'Oui':
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
            
            
    def driveTournament(self, tournament):
            print('\n\n--------------------------------------------------------------------')
            print(f"                  Etapes du tournoi {tournament.name} \n")
            table3 =[["Création", "Joueurs"]]
            table3.append(["---V---"])  
            if tournament.actualRound != 0 :
                table3[1].append("---V---")
            else : 
                table3[1].append("---X---")
            for round in tournament.roundList:
                table3[0].append(f"{round.name}")
                if round.endDate:
                    table3[1].append("---V---")
                else : 
                    table3[1].append("---X---")
            table3[0].append("Cloture")
            if tournament.endDate:
                table3[1].append("---V---")
            else : 
                table3[1].append("---X---")
            print(tabulate(table3, headers="firstrow"))
            
    def addPlayer(self, table, table2, tournament, FFEList):
        print('\n\n--------------------------------------------------------------------')
        print(f"          Ajouter des joueurs au tournoi : {tournament.name} \n\n")
        print("                   Liste des joueurs du club         ")
        print(tabulate(table, headers="firstrow"))
        print("\n\n")
        print("                   Liste des joueurs du tournoi")
        print(tabulate(table2, headers="firstrow"))
        print("\n")
        nrFFE = None
        while nrFFE not in FFEList:
                nrFFE = input("\nQuand tous les joueurs sont ajoutés notez 'Terminé'\nQuel est le N° FFE du joueur à ajouter : ")
        return nrFFE