data = list(map(int, open("input.txt").readlines()))
increases = sum(cur < nxt for cur, nxt in zip(data, data[1:]))
print(increases)
