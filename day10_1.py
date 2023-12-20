up = "J|L"
left = "J-7"
down = "7|F"
right = "L-F"

diagram = []
with open("day10.txt") as file:
    for i, line in enumerate(file):
        diagram.append(line.strip())
        j = line.find("S")
        if j >= 0:
            start = (i, j)

def get(i, j):
    if 0 <= i and i < len(diagram) and 0 <= j and j < len(diagram[0]):
        return diagram[i][j]
    else:
        return "X"
def mark(i, j):
    diagram[i] = diagram[i][:j] + "X" + diagram[i][j+1:]

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
        queue_top = (i-1, j)
    if get(i, j) in left and get(i, j-1) in right:
        mark(i, j)
        queue_top = (i, j-1)
    if get(i, j) in down and get(i+1, j) in up:
        mark(i, j)
        queue_top = (i+1, j)
    if get(i, j) in right and get(i, j+1) in left:
        mark(i, j)
        queue_top = (i, j+1)
    
    assert((i,j) != queue_top)
    queue_top, queue_other = queue_other, queue_top
    distance2 += 1

for line in diagram:
    print(line)
print(distance2//2)
