from itertools import chain
from pprint import pprint
from re import split as re_split

def prepare(data):
    draws, *boards = re_split(r"(?m)^$", data.strip())
    draws = draws.strip().split(",")
    boards = [[line.strip().split() for line in board.strip().split("\n")] for board in boards]
    return draws, boards

def remove_draw(board, d):
    removed_coords = []
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num == d:
                row[j]= None
                removed_coords.append((i, j))
                
    return removed_coords

def empty_row_or_col(board, x, y):
    return not any(board[x]) or not any(row[y] for row in board)
    
def sum_board(board):
    return sum(int(n) for n in chain.from_iterable(board) if n is not None)

def solve():
    data = open("input.txt").read()
    draws, boards = prepare(data)
    
    for i, draw in enumerate(draws):
        for j, board in enumerate(boards):
            removed_coords = remove_draw(board, draw)
            
            if i >= 4:
                if removed_coords and any(empty_row_or_col(board, x, y) for x, y in removed_coords):
                    print(f"Winning board: #{1 + j}\n")
                    pprint(board)
                    print(int(draw) * sum_board(board))
                    return
               
if __name__ == "__main__":
    solve()