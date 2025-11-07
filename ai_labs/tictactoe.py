import random

board = [' ' for _ in range(9)]

def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_board_full():
    return ' ' not in board

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

def computer_move():
    for move in range(9):
        if board[move] == ' ':
            board[move] = 'O'
            if check_winner('O'):
                return
            board[move] = ' '
    for move in range(9):
        if board[move] == ' ':
            board[move] = 'X'
            if check_winner('X'):
                board[move] = 'O'
                return
            board[move] = ' '
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            board[move] = 'O'
            break

def play_game():
    display_board()
    while True:
        # Player's turn
        player_move()
        display_board()
        if check_winner('X'):
            print("Congratulations! You win!")
            break
        if is_board_full():
            print("It's a tie!")
            break

        # Computer's turn
        computer_move()
        display_board()
        if check_winner('O'):
            print("Computer wins! Better luck next time.")
            break
        if is_board_full():
            print("It's a tie!")
            break

play_game()
