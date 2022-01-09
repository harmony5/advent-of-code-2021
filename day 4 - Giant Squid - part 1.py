from itertools import chain, product
from pprint import pprint
from typing import TypeAlias, TypeVar


T = TypeVar("T")
Board: TypeAlias = list[list[T]]
Num: TypeAlias = int | str


def remove_draw(board: Board[Num], draw: Num) -> tuple[int, int]:
    removed_coords = []
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num == draw:
                row[j] = 0
                removed_coords.append((i, j))

    return removed_coords


def empty_row_or_col(board: Board[Num], x: int, y: int) -> bool:
    return not any(board[x]) or not any(row[y] for row in board)


def sum_board(board: Board[Num]) -> int:
    # flatten = chain.from_iterable
    return sum(int(n) for n in chain.from_iterable(board))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()

    draws, *boards = data.strip().split("\n\n")
    draws = draws.strip().split(",")
    boards = [
        [line.strip().split() for line in board.strip().split("\n")] for board in boards
    ]

    for draw, board in product(draws, boards):
        removed_coords = remove_draw(board, draw)

        if removed_coords and any(
            empty_row_or_col(board, x, y) for x, y in removed_coords
        ):
            print(f"Winning board:\n")
            pprint(board)
            print(int(draw) * sum_board(board))
            break
