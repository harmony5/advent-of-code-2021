from itertools import chain
from pprint import pprint


def remove_draw(board, draw):
    for row in board:
        for j, num in enumerate(row):
            if num == draw:
                row[j] = 0


def empty_row_or_col(board, x, y):
    return not any(board[x]) or not any(row[y] for row in board)


def is_winning_board(board):
    return any(empty_row_or_col(board, i, i) for i in range(len(board)))


def sum_board(board):
    # flatten = chain.from_iterable
    return sum(map(int, chain.from_iterable(board)))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()

    draws, *boards = data.strip().split("\n\n")
    draws = draws.strip().split(",")
    boards = [
        [line.strip().split() for line in board.strip().split("\n")] for board in boards
    ]

    # board, draw * board sum
    last_winning_board = ([], 0)
    for i, draw in enumerate(draws):
        remaining_boards = [b for b in boards if not is_winning_board(b)]

        if not remaining_boards:
            break

        for board in remaining_boards:
            remove_draw(board, draw)

            if i >= 4 and is_winning_board(board):
                last_winning_board = board, int(draw) * sum_board(board)

    pprint(last_winning_board[0])
    print(last_winning_board[1])
