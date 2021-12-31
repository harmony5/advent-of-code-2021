from itertools import chain, tee
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
                row[j] = None
                removed_coords.append((i, j))

    return removed_coords


def empty_row_or_col(board, x, y):
    return not any(board[x]) or not any(row[y] for row in board)


def sum_board(board):
    return sum(int(n) for n in chain.from_iterable(board) if n is not None)


def solve():
    with open("input.txt") as f:
        data = f.read()
    draws, boards = prepare(data)

    # board, draw * board sum
    last_winning_board = ([], 0)
    for i, draw in enumerate(draws):
        # remove boards that have already won
        filtered_boards = [
            b
            for b in boards
            if not any(empty_row_or_col(b, x, y) for x, y in zip(*tee(range(5))))
        ]
        if not filtered_boards:
            break

        for board in filtered_boards:
            removed_coords = remove_draw(board, draw)

            if i >= 4:
                # check if the current board wins this round with the current draw
                if removed_coords and any(
                    empty_row_or_col(board, x, y) for x, y in removed_coords
                ):
                    last_winning_board = board, int(draw) * sum_board(board)

    pprint(last_winning_board[0])
    print(last_winning_board[1])


if __name__ == "__main__":
    solve()
