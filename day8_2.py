nodes = dict()
with open("day8.txt") as file:
    instructions = file.readline().strip()
    file.readline()
    for line in file:
        i = line[0:3]
        left = line[7:10]
        right = line[12:15]
        nodes[i] = (left, right)

cycles = []
for location in nodes.keys():
    if location[2] == "A":
        original_location = location
        #destination = location[0:2]+"Z"
        steps = 0
        #while location != destination:
        while location[2] != "Z":
            for i, c in enumerate(instructions):
                node = nodes[location]
                if c == "L":
                    location = node[0]
                else:
                    location = node[1]
                #if location == destination:
                if location[2] == "Z":
                    break
            steps += i+1
            print(original_location, steps)
        print(steps)
        cycles.append(steps)
print(cycles)
global_cycle = 1
for cycle in cycles:
    gcd = global_cycle
    b = cycle
    while b != 0:
        gcd = gcd % b
        gcd, b = b, gcd
    global_cycle = global_cycle * cycle // gcd
    print(global_cycle)
