from itertools import chain

flatten = chain.from_iterable


class Board:
    """Class defining a 2D bingo board"""

    def __init__(self, rows):
        self.__rows = rows

    @property
    def is_winner(self):
        """A board wins if any of its rows or columns is empty"""
        return any(
            self.is_empty_row(i) or self.is_empty_col(i) for i in range(len(self))
        )

    def __getitem__(self, index):
        return self.__rows[index]

    def __len__(self):
        return len(self.__rows)

    def __str__(self):
        return "\n".join(" ".join(str(col).rjust(3) for col in row) for row in self)

    def __repr__(self):
        return f"Board({self.__rows})"

    def remove_draw(self, draw):
        """Remove a draw from the board"""
        for row in self:
            for j, col in enumerate(row):
                if col == draw:
                    row[j] = 0

    def is_empty_row(self, row):
        """Check if the row is empty"""
        return not any(self[row])

    def is_empty_col(self, col):
        """Check if the column is empty"""
        return not any(row[col] for row in self)


def prepare(data):
    draws, *boards = data.strip().split("\n\n")
    draws = draws.strip().split(",")
    boards = [
        Board([line.strip().split() for line in board.strip().split("\n")])
        for board in boards
    ]
    return draws, boards


def sum_board(board):
    return sum(map(int, flatten(board)))


if __name__ == "__main__":
    with open("input.txt") as f:
        data = f.read()

    draws, boards = prepare(data)

    # board, draw * board sum
    last_winning_board = ([], 0)
    for draw in draws:
        remaining_boards = [b for b in boards if not b.is_winner]

        if not remaining_boards:
            break

        for board in remaining_boards:
            board.remove_draw(draw)

            if board.is_winner:
                last_winning_board = board, int(draw) * sum_board(board)

    print(last_winning_board[0])
    print(last_winning_board[1])
