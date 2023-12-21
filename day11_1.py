import numpy
import re

sky = []
s = 0
with open("day11.txt") as file:
    for line in file:
        line = line.strip()
        sky.append(line)
        if line.count("#") == 0:
            sky.append(line)

#transpose
sky = ["".join(line) for line in zip(*sky)]

print()
sky2 = []
for line in sky:
    sky2.append(line)
    if line.count("#") == 0:
        sky2.append(line)
sky = sky2

##transpose
#sky = ["".join(line) for line in zip(*sky)]

galaxies = []
for i, line in enumerate(sky):
    for m in re.finditer("#", line):
        galaxies.append(numpy.array((i,m.start())))

s = 0
for i, galaxy in enumerate(galaxies):
    for galaxy2 in galaxies[i+1:]:
        print(galaxy, galaxy2, galaxy-galaxy2, abs(galaxy-galaxy2))
        s += sum(abs(galaxy-galaxy2))

print(s)
