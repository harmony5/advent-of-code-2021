from itertools import islice, starmap, tee
from operator import lt

# solution inspired by https://mathspp.com/blog/advent-of-code-sonar-sweep-analysis

with open("input.txt") as f:
    data = (int(line) for line in f.readlines())

curs, nexts = tee(data)
nexts = islice(nexts, 3, None)
increases = sum(starmap(lt, zip(curs, nexts)))

print(increases)
