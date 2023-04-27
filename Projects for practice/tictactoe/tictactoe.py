import time
import random
import os

board = ["A"," "," "," "," "," "," "," "," ", " ", " "]
player = "X"
player2 = "O"
players = ["Player", "Player2"]

win = None
numbers = None

def main():
    print("Welcome to the Tictactoe game in python!")
    print("List of game modes: \n-Play with bot \n-Play with other player \n-Tutorial \n-Options\n-Close\n\n")
    time.sleep(2)
    selected_game = input("What mode you want to play? ")
    option_selected = menu_options.get(selected_game)
    if option_selected is None:
        print("Error, you don't select a valid option, please try again!")
        time.sleep(5)
        os.system("cls")
        main()
    else:
        option_selected()

def first_player():
    global random_select
    random_select = random.choice(players)
    print(f"Empieza el jugador '{random_select}'")

def bot_game():
    global win
    print("Welcome to Bot game, renember you use X and bot use O")
    first_player()
    while win != "Player" and win != "Player2" and win != "Draw":
        if random_select == "Player":
            turn_player()
            turn_bot()
        else:
            turn_bot()
            turn_player()
    if win == "Player":
        print("Congratulations you win Bot game!")
        print("This is the board:")
        print_board()
    elif win == "Player2":
        print("Sorry, but you lose Bot game")
        print("This is the board:")
        print_board()
    elif win == "Draw":
        print("Draw!!!!!!!")
        print("This is the board:")
        print_board()
def turn_player():
    print("Your turn Player1!")
    print_board()
    board_selected = str(input("What space you want to use? "))
    board_used_checker(board_selected)
    board_selected = board_selected + "x"
    board_updater(board_selected)
    win_checker()
    os.system("cls")

def turn_player2():
    print("Your turn Player2!")
    print_board()
    board_selected = str(input("What space you want to use? "))
    board_selected = board_selected + "o"
    board_updater(board_selected)
    win_checker()
    os.system("cls")

def turn_bot():
    valid_spaces_confirmer = None
    print("Bot turn")
    print_board()
    print("The bot thinks...")
    while valid_spaces_confirmer != True:
        board_selected = random.randint(1,9)
        if board[board_selected] == " ":
            valid_spaces_confirmer = True

    board_selected = str(board_selected)
    board_selected = board_selected + "o"
    board_updater(board_selected)
    win_checker()
    draw_check()
    print(win)
    os.system("cls")

def board_updater(selected):
    global board
    if "x" in selected:
        selected = selected.replace("x", "")
        selected = int(selected)
        for i in range(1,9):
            if selected == board[i] == "X":
                print("You select a occupied space, please try again")
                print("Restarting game...")
                pass
        board[selected] = "X"
    elif "o" in selected:
        selected = selected.replace("o", "")
        selected = int(selected)
        for i in range(1,9):
            if selected == board[i] == "O":
                print("You select a occupied space, please try again")
                print("Restarting game")
        board[selected] = "O"

def print_board():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7],board[8],board[9]))
    print("   |   |   ")

def rows_check():
    global win
    row_1_player = board[1] == board[2] == board[3] != " "
    row_2_player = board[4] == board[5] == board[6] != " "
    row_3_player = board[7] == board[8] == board[9] != " "

    if row_1_player or row_2_player or row_3_player:
        for i in range(1, 8, 3):
            if board[i] == board[i + 1] == board[i + 2] == "X":
                win = "Player"
                break
            elif board[i] == board[i + 1] == board[i + 2] == "O":
                win = "Player2"
                break
        
def columns_check():
    global win
    col_1 = board[1] == board[4] == board[7] != " "
    col_2 = board[2] == board[5] == board[8] != " "
    col_3 = board[3] == board[6] == board[9] != " "
    if col_1 or col_2 or col_3:
        for i in range(0, 3):
            if board[3 - i] == board[6 - i] == board[9 - i] == "X":
                win = "Player"
                break
            elif board[3 - i] == board[6 - i] == board[9 - i] == "O":
                win = "Player2"
                break

def diagonals_check():
    global win
    dia_1 = board[1] == board[5] == board[9] != " "
    dia_2 = board[3] == board[5] == board[7] != " "
    if dia_1 or dia_2:
        win = "Player" if board[1] == board[5] == board[9] == "X" or board[3] == board[5] == board[7] == "X" else "Player2"

def board_used_checker(selected):
    selected = int(selected)
    if board[selected] != " ":
        print("Please select a valid space")
        print("Deleting the game...")
        print("Error 'No valid space selected', returning to menu")
        os.system("cls")
        main()

def valid_spaces():
    global valid_spaces_board
    valid_spaces_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(1,9):
        if board[i] != " ":
            valid_spaces_board = valid_spaces_board.remove(i)

def draw_check():
    global win
    if " " not in board:
        win = "Draw"
    print("Draw_check func")

def win_checker():
    global win
    rows_check()
    columns_check()
    diagonals_check()

menu_options = {
    "Play with bot" : bot_game,
    "Play with other player" : None,
    "Tutorial" : None,
    "Options" : None,
    "Close" : exit,
}

if __name__ == "__main__":
    main()