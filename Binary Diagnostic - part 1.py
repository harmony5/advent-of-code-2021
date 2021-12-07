from functools import reduce
data = open("input.txt").readlines()

# transpose
data = [*zip(*data)]

gamma = 0
for line in data:
    gamma <<= 1
    gamma += line.count("1") > line.count("0")

# invert gamma and remove sign bit
epsilon = ~gamma + (1 << gamma.bit_length())

print(f"{gamma=}; {epsilon=}")
print(gamma * epsilon)


# alternative, few liner, garbled solution
g = reduce(lambda acc, line: (acc << 1) + (line.count("1") > line.count("0")), data, 0)
e = ~g + (1 << g.bit_length())
print(f"{g=}; {e=}\n{g*e}")