from statistics import mode as most_common

with open("input.txt") as f:
    data = f.readlines()

gamma = "".join(map(most_common, zip(*data)))
gamma = int(gamma, 2)

# invert gamma and remove sign bit
epsilon = ~gamma + 2 ** gamma.bit_length()

print(f"{gamma=}; {epsilon=}; {gamma * epsilon=}")
