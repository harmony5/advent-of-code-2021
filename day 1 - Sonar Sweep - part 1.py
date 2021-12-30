with open("input.txt") as f:
    data = [int(line) for line in f.readlines()]

increases = sum(cur < nxt for cur, nxt in zip(data, data[1:]))
print(increases)
