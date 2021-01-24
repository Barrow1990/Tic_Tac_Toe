icons = {
    "blank": ["      ", "      ", "      ", "      ", "      "],
    "o": [" **** ", "*    *", "*    *", "*    *", " **** "],
    "ex":   ["*    *", " *  * ", "  **  ", " *  * ", "*    *"]
}


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def blank_square():
    for i in icons["blank"]:
        print(i)


def circle_basic():
    for i in icons["circle"]:
        print(i)


def x_basic():
    for i in icons["ex"]:
        print(i)


def grid(game_grid):

    separators = (" -" + "-" * 26 + "-")
    center_columns = " | "
    outer_columns = " | "

    print(separators)

    for num in range(5):
        top = (outer_columns + game_grid_data[0]["item"][num] + center_columns + game_grid_data[1]["item"][num]
               + center_columns + game_grid_data[2]["item"][num] + outer_columns)
        print(top)

    print(separators)

    for num in range(5):
        middle = (outer_columns + game_grid_data[3]["item"][num] + center_columns +
                  game_grid_data[4]["item"][num] + center_columns + game_grid_data[5]["item"][num] +
                  outer_columns)
        print(middle)

    print(separators)

    for num in range(5):
        bottom = (outer_columns + game_grid_data[6]["item"][num] + center_columns +
                  game_grid_data[7]["item"][num] + center_columns + game_grid_data[8]["item"][num] +
                  outer_columns)
        print(bottom)

    print(separators)


def print_message(*message, width=50, header=True):
    screen = []
    screen.append("-" * width + "\n")
    word_count = 1
    for word in message:
        spacesstart = 2
        spacesend = int(width - len(word) - 2 - 2)
        if header is True and word_count == 1:
            spacesstart = spacesend = int((width - len(word) - 2) / 2)
            if len(word) % 2 != 0:
                spacesend += 1
        line = []
        line.append("|" + " " * spacesstart)
        for letter in word:
            line.append(letter)
        line.append(" " * spacesend + "|")
        line.append("\n")
        screen.append(line)
        word_count += 1
    screen.append("-" * width + "\n")

    for word in screen:
        for letter in word:
            print(letter, end="")


def main_menu():
    print_message("Welcome To Tik Tac Toe",
                  " ",
                  "Menu:",
                  "1: 1 Player",
                  "2: 2 Player",
                  "3: Help",
                  "4: Testing",
                  " ",
                  "0: Exit",
                  width=50, header=True)


def player_setup(players):
    if players == 1:
        p1 = input("Whats the Name for Player 1?: ")
        p2 = "Computer"
    else:
        p1 = input("Whats the Name for Player 1?: ")
        p2 = input("Whats the Name for Player 2?: ")

    players_data["player1"]["name"], players_data["player2"]["name"] = p1, p2


def validate_move(player_choice, x):
    if player_choice > 9:
        print("Please Enter a number Between 1 and 9")
        return False
    if game_grid_data[player_choice - 1]["item"] == icons['blank']:
        game_grid_data[player_choice - 1]["item"] = players_data[f"player{x}"]["token"]
        return True
    else:
        print("This Space is Already Taken")
        return False


def game(players):
    playing = True
    round = 1
    while playing:
        for x in range(1, 3):
            grid(game_grid_data)
            player_name = players[f"player{x}"]["name"]

            if player_name == "Computer":
                print("Computer Is Moving")
            player_choice = int(input(f"{player_name}, Your Turn: "))
            validated = validate_move(player_choice, x)

            while validated is False:
                player_choice = int(input(f"{player_name}, Your Turn: "))
                validated = validate_move(player_choice, x)
            grid(game_grid_data)

            round += 1
            if round > 3:
                continue
                result = win_or_lose()
                playing = result
            elif round == 10:
                print("Tie Break")
                playing = False
                break


def game_menu():
    running = True
    while running:
        # Run Menu
        main_menu()
        menu_choice = int(input("Please Choose An Option: "))
        if menu_choice == 0:
            print("Thank You For Playing")
            print("Goodbye")
            break
        elif menu_choice == 1:
            player_setup(1)
            game(players_data)
        elif menu_choice == 2:
            player_setup(2)
            game(players_data)
        elif menu_choice == 3:
            print("menu_choice 3")


def win_or_lose():  # Still need to sort out
    for i in range(0, 9, 3):
        if icons['blank'] not in (game_grid_data[i]["item"], game_grid_data[i + 1]["item"], game_grid_data[i + 2]["item"]) and \
           icons['ex'] is (game_grid_data[i]["item"], game_grid_data[i + 1]["item"], game_grid_data[i + 2]["item"]):
            print("Congrats")
            continue
        else:
            print("blanks in row")
            break
    for i in range(0, 3):
        if icons['blank'] not in (game_grid_data[i]["item"], game_grid_data[i + 3]["item"], game_grid_data[i + 6]["item"]):
            print("No Blanks in column")
            continue
        else:
            print("blanks in column")
            break
    if icons['blank'] not in (game_grid_data[0]["item"], game_grid_data[4]["item"], game_grid_data[8]["item"]) or \
       icons['ex'] not in (game_grid_data[2]["item"], game_grid_data[4]["item"], game_grid_data[6]["item"]):
        print("No Blanks in Diagnal")
    else:
        print("Blanks in Diagnal")    

game_grid_data = {
    0: {"name": "top_left", "item": icons['blank']},
    1: {"name": "top_middle", "item": icons['blank']},
    2: {"name": "top_right", "item": icons['blank']},
    3: {"name": "middle_left", "item": icons['blank']},
    4: {"name": "middle_middle", "item": icons['blank']},
    5: {"name": "middle_right", "item": icons['blank']},
    6: {"name": "bottom_left", "item": icons['blank']},
    7: {"name": "bottom_middle", "item": icons['blank']},
    8: {"name": "bottom_right", "item": icons['blank']}
}


p1 = "Chris"
p2 = "Cat"
players_data = {
    "player1": {"name": p1,
                "token": icons["ex"]},
    "player2": {"name": p2,
                "token": icons["o"]}}

game_menu()
