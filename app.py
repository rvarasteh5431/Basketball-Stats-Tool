import constants
import copy

players = []
panthers = []
bandits = []
warriors = []
experienced_players = []
inexperienced_players = []


def clean_up():
    con_copy = copy.deepcopy(constants.PLAYERS)
    for player in con_copy:
        for key, value in player.items():
            if key == "height":
                height = int(value.split()[0])
                player["height"] = height
        for key, value in player.items():
            if key == "experience":
                if value == "YES":
                    value = True
                    player["experience"] = value
                elif value == "NO":
                    value = False
                    player["experience"] = value
        for key, value in player.items():
            if key == "guardians":
                guard = value.split(" and ")
                player["guardians"] = guard
        players.append(player)


def balance():
    counter = 0
    for player in players:
        for key, value in player.items():
            if key == "experience":
                if value is True:
                    experienced_players.append(player)
                elif value is False:
                    inexperienced_players.append(player)
    for player in experienced_players:
        if counter == 0:
            panthers.append(player)
            counter = 1
        elif counter == 1:
            bandits.append(player)
            counter = 2
        elif counter == 2:
            warriors.append(player)
            counter = 0
    for player in inexperienced_players:
        if counter == 0:
            panthers.append(player)
            counter = 1
        elif counter == 1:
            bandits.append(player)
            counter = 2
        elif counter == 2:
            warriors.append(player)
            counter = 0


def displays(team_name, list_of_players):
    print("\nTeam: {} Stats".format(team_name))
    print("--------------------")
    print("Total players: {}".format(len(list_of_players)))
    experienced = 0
    for player in list_of_players:
        for key, value in player.items():
            if key == "experience":
                if value is True:
                    experienced += 1
    print("Total experienced: {}".format(experienced))
    inexperienced = 0
    for player in list_of_players:
        for key, value in player.items():
            if key == "experience":
                if value is False:
                    inexperienced += 1
    print("Total inexperienced: {}".format(inexperienced))
    total_height = 0
    for player in list_of_players:
        for key, value in player.items():
            if key == "height":
                total_height += value
    ave_height = total_height // len(list_of_players)
    print("Average height: {}".format(ave_height))
    print("\nPlayers on Team:")
    teammate = ""
    for player in list_of_players:
        for key, value in player.items():
            if key == "name":
                teammate += value + ", "
    print(teammate)
    print("\nGuardians:")
    guardians = ""
    for player in list_of_players:
        for key, value in player.items():
            if key == "guardians":
                for each in value:
                    guardians += each + ", "
    print(guardians)


def menu():
    print("BASKETBALL TEAM STATS TOOL\n")
    while True:
        try:
            print("----MENU----\n")
            choice_1 = int(
                input("""Here are your choices:\n 1) Display Team Stats\n 2) Quit
\n\nEnter an option > """))
            if choice_1 == 1:
                while True:
                    try:
                        choice_2 = int(
                            input("""\n 1) Panthers\n 2) Bandits\n 3) Warriors
\n 4) Quit\n\nEnter an option > """))
                        if choice_2 == 1:
                            name = "Panthers"
                            displays(name, panthers)
                            input("\nPress ENTER to continue...\n")
                        elif choice_2 == 2:
                            name = "Bandits"
                            displays(name, bandits)
                            input("\nPress ENTER to continue...\n")
                        elif choice_2 == 3:
                            name = "Warriors"
                            displays(name, warriors)
                            input("\nPress ENTER to continue...\n")
                        elif choice_2 == 4:
                            break
                    except ValueError:
                        print("Please enter a valid option... ")
            elif choice_1 == 2:
                break
        except ValueError:
            print("Please enter a valid option... ")


if __name__ == "__main__":
    clean_up()
    balance()
    menu()
