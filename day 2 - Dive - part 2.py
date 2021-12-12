from collections import defaultdict

data = open("input.txt").readlines()
commands = defaultdict(int)

for line in data:
    cmd, value = line.split()
    commands[cmd] += int(value)
    if cmd == "forward":
        commands["depth"] += int(value) * (commands["down"] - commands["up"])

result = commands["forward"] * commands["depth"]
print(result)