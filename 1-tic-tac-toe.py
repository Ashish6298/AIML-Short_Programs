#tictactoe

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print("|{}|{}|{}|".format(board[i], board[i+1], board[i+2]))
    print()

def player_move(icon):
    print(f"Your turn, player {'1' if icon == 'X' else '2'}")
    while True:
        choice = int(input("Enter the value (1-9): ").strip()) - 1
        if board[choice] == " ":
            board[choice] = icon
            break
        else:
            print("Space is already taken")

def victory(icon):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
    return any(all(board[i] == icon for i in combo) for combo in win_combinations)

def draw():
    return " " not in board

while True:
    for icon in "XO":
        print_board()
        player_move(icon)
        if victory(icon):
            print_board()
            print(f"{icon} wins!")
            exit()
        if draw():
            print_board()
            print("It's a draw!")
            exit()
