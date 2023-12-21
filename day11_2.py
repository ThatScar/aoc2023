import numpy
import re

expansion = 999999

sky = []
galaxies_t = [] #transposed: (j i)
empty_row_count = 0
with open("day11.txt") as file:
    for i, line in enumerate(file):
        line = line.strip()
        sky.append(line)
        empty = True
        for m in re.finditer("#", line):
            empty = False
            galaxies_t.append((m.start(),i + empty_row_count * expansion))
        if empty:
            empty_row_count += 1

galaxies_t = [numpy.array(pos) for pos in sorted(galaxies_t)]

#transpose sky
sky = ["".join(line) for line in zip(*sky)]

cursor = 0
empty_column_count = 0
for j, line in enumerate(sky + ["."]): #empty column at the end
    if line.count("#") == 0:
        while cursor < len(galaxies_t) and galaxies_t[cursor][0] < j:
            galaxies_t[cursor][0] += empty_column_count * expansion
            cursor += 1
        empty_column_count += 1

s = 0e1 #scalar overflow with integer
for i, galaxy in enumerate(galaxies_t):
    for galaxy2 in galaxies_t[i+1:]:
        #print(galaxy, galaxy2, galaxy-galaxy2, abs(galaxy-galaxy2))
        s += sum(abs(galaxy-galaxy2))

print(s)

