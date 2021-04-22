# This program is a Game of Tic Tac Toe.
# It was produced during PCEP Certification

from random import choice

icons = {
    "blank": ["      ", "      ", "      ", "      ", "      "],
    "o": [" **** ", "*    *", "*    *", "*    *", " **** "],
    "ex":   ["*    *", " *  * ", "  **  ", " *  * ", "*    *"],
    1: ["  **  ", "  **  ", "  **  ", "  **  ", "  **  "],
    2: ["******", "   ** ", "  **  ", " **   ", "******"],
    3: ["******", "    **", "  ****", "    **", "******"],
    4: ["    * ", "  * * ", " *  * ", "******", "    * "],
    5: ["******", "**    ", "******", "    **", "******"],
    6: ["*     ", "*     ", "******", "*    *", "******"],
    7: ["******", "    * ", "   *  ", "  *   ", " *    "],
    8: ["******", "*    *", "******", "*    *", "******"],
    9: ["******", "*    *", "******", "     *", "     *"]
}


def blank_square():
    for i in icons["blank"]:
        print(i)


def circle():
    for i in icons["circle"]:
        print(i)


def ex():
    for i in icons["ex"]:
        print(i)


def grid(game_grid):

    separators = (" -" + "-" * 26 + "-")
    center_columns = " | "
    outer_columns = " | "

    print(separators)

    # Prints the Top Row of the game taking into account the icon
    for num in range(5):
        top = (outer_columns + game_grid_data[0]["item"][num] + center_columns
               + game_grid_data[1]["item"][num] + center_columns
               + game_grid_data[2]["item"][num] + outer_columns)
        print(top)

    print(separators)

    # Prints the Middle Row of the game taking into account the icon
    for num in range(5):
        middle = (outer_columns + game_grid_data[3]["item"][num]
                  + center_columns + game_grid_data[4]["item"][num]
                  + center_columns + game_grid_data[5]["item"][num]
                  + outer_columns)
        print(middle)

    print(separators)

    # Prints the Bottom Row of the game taking into account the icon
    for num in range(5):
        bottom = (outer_columns + game_grid_data[6]["item"][num]
                  + center_columns + game_grid_data[7]["item"][num]
                  + center_columns + game_grid_data[8]["item"][num]
                  + outer_columns)
        print(bottom)

    print(separators)


def print_message(*message, width=50, header=True):
    # Message: THe full message that is to be displayed on screen
    # Width: The width of the menu on screen
    # Header: Is the first line going to be a header aka in centre

    # Screen is the blank variable to be printed out on screeen later
    screen = []
    screen.append("-" * width + "\n")

    # Word Count for determining if header or not
    word_count = 1

    # Iterates through the message and sorts the output to be within box
    for word in message:
        # How many spaces are at the start before the word starts
        spacesstart = 2
        # Works out how many spaces are at the end of the word
        spacesend = int(width - len(word) - 2 - 2)
        # If header is True then it will iterate through the first line
        # and output it centre in the box.
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

    # Prints out whats on screen
    for word in screen:
        for letter in word:
            print(letter, end="")


def main_menu():
    # Text to display on the main menu.
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
        game_grid_data[player_choice - 1]["item"] = \
            players_data[f"player{x}"]["token"]
        return True
    else:
        print("This Space is Already Taken")
        return False


def game(players):
    playing = True
    turns = 0
    while playing is True:
        for x in range(1, 3):  # Iterates through the 2 players
            if playing is False:
                break

            grid(game_grid_data)  # Prints out the game grid
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
                    print_message(
                        " ",
                        "Tie Match",
                        " ",
                        width=20, header=False)
                else:
                    print_message(
                        " ",
                        f"The Winner is {winner}",
                        " ",
                        width=30, header=False
                    )
                playing = False
                clear_grid()
                break


def game_menu():
    running = True
    while running:
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
            menu_help()


def win_or_lose(players, x, turns):  # Still need to sort out
    player_name = players[f"player{x}"]["name"]
    player_icon = players[f"player{x}"]["token"]
    x = 0

    # Check if any Horizontal Match
    if player_icon is game_grid_data[x]["item"] and player_icon is \
            game_grid_data[x + 1]["item"] and player_icon is \
            game_grid_data[x + 2]["item"] or player_icon is \
            game_grid_data[x + 3]["item"] and player_icon is \
            game_grid_data[x + 4]["item"] and player_icon is \
            game_grid_data[x + 5]["item"] or player_icon is \
            game_grid_data[x + 6]["item"] and player_icon is \
            game_grid_data[x + 7]["item"] and player_icon is \
            game_grid_data[x + 8]["item"]:
        return True, player_name

    # Check if any Vertical Match
    elif player_icon is game_grid_data[x]["item"] and player_icon is \
            game_grid_data[x + 3]["item"] and player_icon is \
            game_grid_data[x + 6]["item"] or player_icon is \
            game_grid_data[x + 1]["item"] and player_icon is \
            game_grid_data[x + 4]["item"] and player_icon is \
            game_grid_data[x + 7]["item"] or player_icon is \
            game_grid_data[x + 2]["item"] and player_icon is \
            game_grid_data[x + 5]["item"] and player_icon is \
            game_grid_data[x + 8]["item"]:
        return True, player_name

    # Check if any Diagnal Match
    elif player_icon is game_grid_data[x]["item"] and player_icon is \
            game_grid_data[x + 4]["item"] and player_icon is \
            game_grid_data[x + 8]["item"] or player_icon is \
            game_grid_data[x + 2]["item"] and player_icon is \
            game_grid_data[x + 4]["item"] and player_icon is \
            game_grid_data[x + 6]["item"]:
        return True, player_name

    # If 9 turns (which is all moves) Then End Game
    elif turns == 9:
        return True, None

    return False, None


def available_moves():
    available_moves = []
    for x in range(9):
        if game_grid_data[x]["item"] is icons[x + 1]:
            available_moves.append(x + 1)

    return available_moves


def clear_grid():
    for x in range(9):
        game_grid_data[x]["item"] = icons['blank']


def menu_help():
    # Text to display on the main menu.
    print_message(
        "Help",
        " ",
        "To Play Tic Tac Toe:",
        "At the menu choose 1 Player or 2 Player",
        "if choosing 1 player, You will play against the Computer",
        " ",
        "Once in the game.",
        "Choose a square number:",
        "Squares are numbered 1 - 9 from top left to bottom right,",
        "Going Horizontal",
        " ",
        "The winner is Determined when there is 3 in a row "
        "or a diagonal",
        width=78, header=True)

    input("Press Enter To Continue")


game_grid_data = {
    0: {"name": "top_left", "item": icons[1]},
    1: {"name": "top_middle", "item": icons[2]},
    2: {"name": "top_right", "item": icons[3]},
    3: {"name": "middle_left", "item": icons[4]},
    4: {"name": "middle_middle", "item": icons[5]},
    5: {"name": "middle_right", "item": icons[6]},
    6: {"name": "bottom_left", "item": icons[7]},
    7: {"name": "bottom_middle", "item": icons[8]},
    8: {"name": "bottom_right", "item": icons[9]}
}

p1 = ""
p2 = ""
players_data = {
    "player1": {"name": p1,
                "token": icons["ex"]},
    "player2": {"name": p2,
                "token": icons["o"]}}

# Activate The Game
game_menu()
