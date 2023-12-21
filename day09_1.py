import numpy

s = 0
with open("day9.txt") as file:
    for line in file:
        readings = numpy.array([int(x) for x in line.strip().split(" ")])
        #print(readings)
        depth = 0
        while any(readings[depth:] != 0):
            readings[depth+1:] = numpy.diff(readings[depth:])
            depth += 1
            #print(depth, readings)
        #print(depth)
        readings = numpy.append(readings, 0)
        while depth > 0:
            #print(readings)
            depth -= 1
            readings[depth:] = numpy.cumsum(readings[depth:])
        #print(readings)
        #print(readings[-1])
        s += readings[-1]
print(s)
