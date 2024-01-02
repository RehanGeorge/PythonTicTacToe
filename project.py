# TicTacToe Game
initial_game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Function to display the game board
def draw_board(game_board):
    print("-------------")
    for row in game_board:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")
        print("-------------")


def play_game():
    game_over = False
    game_board = initial_game_board
    player_1 = "X"
    player_2 = "O"
    print("Welcome to Tic Tac Toe")
    print("Player 1: X and Player 2: O")
    print("Player 1 will go first")
    player = player_1
    while not game_over:
        draw_board(game_board)
        next_round = player_turn(game_board, player)
        new_board = next_round[0]
        player = next_round[1]
        winner = check_winner(new_board)
        if winner:
            draw_board(new_board)
            print(f"{winner} is the winner!")
            game_over = True
            break
        tie = check_tie(new_board)
        if tie:
            draw_board(new_board)
            print("It's a tie!")
            game_over = True
            break


def player_turn(game_board, player):
    try:
        player_choice = int(input("Enter a number between 1-9: "))
        possible_choices = []
        for row in game_board:
            for cell in row:
                if type(cell) == int:
                    possible_choices.append(cell)

        if player_choice not in possible_choices:
            print("Invalid input. Please enter a number between 1-9")
            player_turn(game_board, player)

        for row in game_board:
            for i in range(len(row)):
                if row[i] == int(player_choice):
                    row[i] = player

        new_player = "O" if player == "X" else "X"
        return [game_board, new_player]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return player_turn(game_board, player)


def check_winner(game_board):
    for row in game_board:
        if row[0] == row[1] == row[2]:
            return row[0]
    for i in range(3):
        if game_board[0][i] == game_board[1][i] == game_board[2][i]:
            return game_board[0][i]
    if game_board[0][0] == game_board[1][1] == game_board[2][2]:
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0]:
        return game_board[0][2]
    return False


def check_tie(game_board):
    for row in game_board:
        for cell in row:
            if type(cell) == int:
                return False
    return True


play_game()
