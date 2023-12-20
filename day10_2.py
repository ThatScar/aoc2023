up = "J|L"
left = "J-7"
down = "7|F"
right = "L-F"

diagram = []
side_diagram = []
with open("day10.txt") as file:
    for i, line in enumerate(file):
        diagram.append(line.strip())
        side_diagram.append("." * len(line.strip()))
        j = line.find("S")
        if j >= 0:
            start = (i, j)
def get_from_diagram(d, i, j):
    if 0 <= i and i < len(d) and 0 <= j and j < len(d[0]):
        return d[i][j]
    else:
        return "X"
def get(i, j):
    return get_from_diagram(diagram, i, j)
def print_on_diagram(d, i, j, c):
    d[i] = d[i][:j] + c + d[i][j+1:]
def mark(i, j):
    print_on_diagram(diagram, i, j, "X")
    print_on_diagram(side_diagram, i, j, "-")
errors = []
def side1(i, j):
    if get_from_diagram(side_diagram, i, j) == "2":
        errors.append((i, j, 1))
    if get(i, j) != "X":
        print_on_diagram(side_diagram, i, j, "1")
def side2(i, j):
    if get_from_diagram(side_diagram, i, j) == "1":
        errors.append((i, j, 2))
    if get(i, j) != "X":
        print_on_diagram(side_diagram, i, j, "2")

i, j = start
queue = []
if get(i-1, j) in down:
    queue.append((i-1, j))
if get(i, j-1) in right:
    queue.append((i, j-1))
if get(i+1, j) in up:
    queue.append((i+1, j))
if get(i, j+1) in left:
    queue.append((i, j+1))

distance2 = 2
queue_top, queue_other = queue
while queue_top != queue_other:
    i, j = queue_top
    if get(i, j) in up and get(i-1, j) in down:
        mark(i, j)
        side1(i, j-1)
        side2(i, j+1)
        queue_top = (i-1, j)
        side1(i-1, j-1)
        side2(i-1, j+1)
    if get(i, j) in left and get(i, j-1) in right:
        mark(i, j)
        side1(i+1, j)
        side2(i-1, j)
        queue_top = (i, j-1)
        side1(i+1, j-1)
        side2(i-1, j-1)
    if get(i, j) in down and get(i+1, j) in up:
        mark(i, j)
        side1(i, j+1)
        side2(i, j-1)
        queue_top = (i+1, j)
        side1(i+1, j+1)
        side2(i+1, j-1)
    if get(i, j) in right and get(i, j+1) in left:
        mark(i, j)
        side1(i-1, j)
        side2(i+1, j)
        queue_top = (i, j+1)
        side1(i-1, j+1)
        side2(i+1, j+1)
    
    assert((i,j) != queue_top)
    queue_top, queue_other = queue_other, queue_top
    side1, side2 = side2, side1
    distance2 += 1
i, j = queue_top
mark(i, j)

for line in side_diagram:
    print(line)

for error in errors:
    i, j, side = error
    if get(i, j) != "X":
        print(error)

count = 0
for line in side_diagram:
    count += line.count("1")
print(count)
# hardcode based on image formed
for i in range(35, 105):
    line = side_diagram[i][35:105]
    print(line)
    count += line.count(".")
print(count)
