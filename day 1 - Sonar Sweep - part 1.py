from operator import lt

with open("input.txt") as f:
    data = [int(line) for line in f.readlines()]

increases = sum(map(lt, zip(data, data[1:])))
print(increases)
