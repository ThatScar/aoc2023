nodes = dict()
with open("day8.txt") as file:
    instructions = file.readline().strip()
    file.readline()
    for line in file:
        i = line[0:3]
        left = line[7:10]
        right = line[12:15]
        nodes[i] = (left, right)

location = "AAA"
steps = 0
while location != "ZZZ":
    for i, c in enumerate(instructions):
        node = nodes[location]
        if c == "L":
            location = node[0]
        else:
            location = node[1]
        if location == "ZZZ":
            break
    steps += i+1
    print(steps)
print(steps)
