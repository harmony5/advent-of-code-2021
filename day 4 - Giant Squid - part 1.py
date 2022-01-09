from itertools import chain, product
from pprint import pprint
from re import split as re_split


def prepare(data):
    draws, *boards = re_split(r"(?m)^$", data.strip())
    draws = draws.strip().split(",")
    boards = [
        [line.strip().split() for line in board.strip().split("\n")] for board in boards
    ]
    return draws, boards


def remove_draw(board, d):
    removed_coords = []
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num == d:
                row[j] = 0
                removed_coords.append((i, j))

    return removed_coords


def empty_row_or_col(board, x, y):
    return not any(board[x]) or not any(row[y] for row in board)


def sum_board(board):
    # flatten = chain.from_iterable
    return sum(int(n) for n in chain.from_iterable(board))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()

    draws, boards = prepare(data)

    for draw, board in product(draws, boards):
        removed_coords = remove_draw(board, draw)

        if removed_coords and any(
            empty_row_or_col(board, x, y) for x, y in removed_coords
        ):
            print(f"Winning board:\n")
            pprint(board)
            print(int(draw) * sum_board(board))
            break
