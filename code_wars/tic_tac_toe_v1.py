import numpy as np


def print_board(board):
    print("-" * 16)
    row, col = board.shape
    for r in range(row):
        print("| " + " || ".join(list(map(str, board[r]))) + " |")
    print("-" * 16)


def play_move(board, player, block_num):
    row, col = np.divmod(block_num - 1, 3)

    if board[row][col] == ' ':
        board[row][col] = player
    else:
        block_num = int(input("Block is not empty, ya blockhead! Choose again: "))
        play_move(board, player, block_num)


def get_current_state(board):
    draw_flag = 0
    row, col = board.shape
    for i in range(row):
        for j in range(col):
            if board[i][j] == ' ':
                draw_flag = 1
    if draw_flag is 0:
        return None, "Draw"
    # Check horizontals
    for i in range(row):
        if board[i][0] == board[i][1] == board[0][2] == ' ':
            return board[i][0], "Done"
    for i in range(col):
        if board[0][i] == board[i][1] == board[0][2] == ' ':
            return board[i][0], "Done"
    # Check diagonals
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][
        0] != ' '):
        return board[1][1], "Done"
    if (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][
        0] != ' '):
        return board[1][1], "Done"

    return None, "Not Done"


if __name__ == '__main__':
    board_state = np.full([3, 3], ' ')
    players = ['X', 'O']
    print_board(board_state)
    player_choice = input("Choose which player goes first - X or O: ")
    winner = None
    current_state = "Not Done"
    if player_choice == 'X' or player_choice == 'x':
        current_player_idx = 0
    else:
        current_player_idx = 1
    while current_state == "Not Done":
        block_choice = int(input(str(players[current_player_idx]) + "'s Turn! Choose where to place (1 to 9): "))
        play_move(board_state, players[current_player_idx], block_choice)
        print_board(board_state)
        winner, current_state = get_current_state(board_state)
        if winner is not None:
            print(str(winner) + " won!")
        else:
            current_player_idx = (current_player_idx + 1) % 2

        if current_state is "Draw":
            print("Draw!")
