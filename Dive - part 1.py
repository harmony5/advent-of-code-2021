from collections import defaultdict

data = open("input.txt").readlines()
commands = defaultdict(int)

for line in data:
    cmd, value = line.split()
    commands[cmd] += int(value)

result = commands["forward"] * (commands["down"] - commands["up"])
print(result)