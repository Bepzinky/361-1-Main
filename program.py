import sys

def clear():
    print("\n" * 50)


def confirm():
    input("\nPress Enter to continue...")


def get_choice(valid):
    choice = input("> ").strip().lower()

    if choice == "b":
        return "back"

    if choice in valid:
        return choice

    print("Invalid selection. Please try again.")
    return None

def confirm_start(settings_summary):
    while True:
        clear()
        print("\nYou selected:\n")
        print(settings_summary)

        choice = input("\nStart game with these settings? (Y/N): ").strip().lower()

        if choice == "y":
            print("\nStarting game...")
            confirm()
            return True
        elif choice == "n" or choice == "b":
            print("\nReturning to previous menu...")
            confirm()
            return False
        else:
            print("Invalid input. Please enter Y or N.")
            confirm()

def menu():
    while True:
        clear()
        print("====================================")
        print("            TIC TAC TOE")
        print("====================================")
        print("1) Play Game")
        print("2) Tutorial")
        print("3) New Features")
        print("4) Exit")
        print("\n(Type 'B' at any time to go back)\n")

        choice = get_choice(["1", "2", "3", "4"])

        if choice == "1":
            play_menu()
        elif choice == "2":
            tutorial()
        elif choice == "3":
            new_features()
        elif choice == "4":
            print("\nThank you for playing!")
            sys.exit()
        elif choice is None:
            confirm()

def play_menu():
    while True:
        clear()
        print("====================================")
        print("              PLAY GAME")
        print("====================================")
        print("1) Player vs Computer")
        print("2) Player vs Player")
        print("3) Back")
        print()

        choice = get_choice(["1", "2", "3"])

        if choice == "1":
            pvc_menu()
        elif choice == "2":
            pvp_setup()
        elif choice == "3" or choice == "back":
            return
        elif choice is None:
            confirm()


def pvc_menu():
    while True:
        clear()
        print("====================================")
        print("        PLAYER VS COMPUTER")
        print("====================================")
        print("Choose Difficulty (affects how smart the computer plays):")
        print("1) Easy")
        print("2) Medium")
        print("3) Hard")
        print("4) Back")
        print()

        choice = get_choice(["1", "2", "3", "4"])

        if choice in ["1", "2", "3"]:
            difficulty_map = {"1": "Easy", "2": "Medium", "3": "Hard"}
            difficulty = difficulty_map[choice]

            symbol = symbol_selection()
            if symbol is None:
                continue

            summary = f"Mode: Player vs Computer\nDifficulty: {difficulty}\nSymbol: {symbol}"

            if confirm_start(summary):
                return

        elif choice == "4" or choice == "back":
            return
        elif choice is None:
            confirm()


def symbol_selection():
    while True:
        clear()
        print("====================================")
        print("         SYMBOL SELECTION")
        print("====================================")
        print("1) X (Goes First)")
        print("2) O (Goes Second)")
        print("3) Back")
        print()

        choice = get_choice(["1", "2", "3"])

        if choice == "1":
            return "X (Goes First)"
        elif choice == "2":
            return "O (Goes Second)"
        elif choice == "3" or choice == "back":
            return None
        elif choice is None:
            confirm()


def pvp_setup():
    while True:
        clear()
        print("====================================")
        print("         PLAYER VS PLAYER")
        print("====================================")
        print("(Type 'B' to go back)\n")

        name1 = input("Enter Player 1 name: ").strip()
        if name1.lower() == "b":
            return

        name2 = input("Enter Player 2 name: ").strip()
        if name2.lower() == "b":
            return

        summary = f"Mode: Player vs Player\nPlayer 1: {name1}\nPlayer 2: {name2}"

        if confirm_start(summary):
            return


def tutorial():
    while True:
        clear()
        print("====================================")
        print("              TUTORIAL")
        print("====================================")
        print("HOW TO PLAY:")
        print("- Tic Tac Toe is played on a 3x3 grid.")
        print("- Players take turns placing X or O.")
        print("- First player to get 3 in a row wins.")
        print("- Rows, columns, and diagonals count.")
        print("- If all spaces fill without a winner,")
        print("- the game ends in a draw.")
        print("\nType 'B' to go back.\n")

        choice = input("> ").strip().lower()
        if choice == "b":
            return


# -------------------- New Features --------------------

def new_features():
    while True:
        clear()
        print("====================================")
        print("            NEW FEATURES")
        print("              Version 1")
        print("====================================")
        print("Added Difficulty Selection")
        print("Added Opponent Selection")
        print("Added New Features Section")
        print("Added Tutorial Section")
        print("Added Symbol Selection")
        print("Added Game Start Confirmation")
        print("\nType 'B' to go back.\n")

        choice = input("> ").strip().lower()
        if choice == "b":
            return



if __name__ == "__main__":
    menu()

