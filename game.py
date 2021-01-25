from random import choice

icons = {
    "blank": ["      ", "      ", "      ", "      ", "      "],
    "o": [" **** ", "*    *", "*    *", "*    *", " **** "],
    "ex":   ["*    *", " *  * ", "  **  ", " *  * ", "*    *"]
}


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
                  "3: Computer vs Computer",
                  "4: Help",
                  " ",
                  "0: Exit",
                  width=50, header=True)


def player_setup(players):
    if players == 1:
        p1 = input("Whats the Name for Player 1?: ")
        p2 = "Computer"
    elif players == 2:
        p1 = input("Whats the Name for Player 1?: ")
        p2 = input("Whats the Name for Player 2?: ")
    elif players == 3:
        p1 = "Computer1"
        p2 = "Computer2"

    players_data["player1"]["name"], players_data["player2"]["name"] = p1, p2


def validate_move(player_choice, x):
    if player_choice > 9:
        print("Please Enter a number Between 1 and 9")
        return False
    if player_choice in available_moves():
        game_grid_data[player_choice - 1]["item"] = players_data[f"player{x}"]["token"]
        return True
    else:
        print("This Space is Already Taken")
        return False


def game(players):
    playing = True
    turns = 0
    while playing is True:
        for x in range(1, 3):
            if playing is False:
                break

            grid(game_grid_data)
            player_name = players[f"player{x}"]["name"]

            if player_name == "Computer1" or player_name == "Computer2":
                player_choice = choice(available_moves())
                validated = validate_move(player_choice, x)
            else:
                validated = False
                while validated is False:
                    player_choice = int(input(f"{player_name}, Your Turn: "))
                    validated = validate_move(player_choice, x)

            turns += 1
            result, winner = win_or_lose(players, x, turns)
            grid(game_grid_data)
            if result is True:
                if winner is None:
                    print("Tie Match")
                else:
                    print("The Winner is", winner)
                playing = False
                clear_grid()
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
            player_setup(3)
            game(players_data)
        elif menu_choice == 4:
            print("menu_choice 3")


def win_or_lose(players, x, turns):  # Still need to sort out
    player_name = players[f"player{x}"]["name"]
    player_icon = players[f"player{x}"]["token"]
    x = 0
    if player_icon is game_grid_data[x]["item"] and player_icon is game_grid_data[x + 1]["item"] and player_icon is game_grid_data[x + 2]["item"] or \
        player_icon is game_grid_data[x + 3]["item"] and player_icon is game_grid_data[x + 4]["item"] and player_icon is game_grid_data[x + 5]["item"] or \
        player_icon is game_grid_data[x + 6]["item"] and player_icon is game_grid_data[x + 7]["item"] and player_icon is game_grid_data[x + 8]["item"]:
        return True, player_name
    elif player_icon is game_grid_data[x]["item"] and player_icon is game_grid_data[x + 3]["item"] and player_icon is game_grid_data[x + 6]["item"] or \
         player_icon is game_grid_data[x + 1]["item"] and player_icon is game_grid_data[x + 4]["item"] and player_icon is game_grid_data[x + 7]["item"] or \
         player_icon is game_grid_data[x + 2]["item"] and player_icon is game_grid_data[x + 5]["item"] and player_icon is game_grid_data[x + 8]["item"]:
        return True, player_name
    elif player_icon is game_grid_data[x]["item"] and player_icon is game_grid_data[x + 4]["item"] and player_icon is game_grid_data[x + 8]["item"] or \
         player_icon is game_grid_data[x + 2]["item"] and player_icon is game_grid_data[x + 4]["item"] and player_icon is game_grid_data[x + 6]["item"]:
        return True, player_name
    elif turns == 9:
        return True, None

    return False, None


def available_moves():
    available_moves = []
    for x in range(9):
        if game_grid_data[x]["item"] is icons['blank']:
            available_moves.append(x + 1)

    return available_moves


def clear_grid():
    for x in range(9):
        game_grid_data[x]["item"] = icons['blank']


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


p1 = ""
p2 = ""
players_data = {
    "player1": {"name": p1,
                "token": icons["ex"]},
    "player2": {"name": p2,
                "token": icons["o"]}}

game_menu()
