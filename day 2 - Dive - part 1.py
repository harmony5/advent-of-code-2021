from collections import defaultdict

with open("input.txt") as f:
    data = f.readlines()

commands = defaultdict(int)

for line in data:
    cmd, value = line.split()
    commands[cmd] += int(value)

result = commands["forward"] * (commands["down"] - commands["up"])
print(result)