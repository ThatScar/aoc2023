import numpy

def extrapolate(sequence):
    if all(sequence == 0):
        return numpy.append(sequence, 0)
    else:
        return numpy.cumsum(numpy.append(sequence[0], extrapolate(numpy.diff(sequence))))

s = 0
with open("day9.txt") as file:
    for line in file:
        readings = numpy.array([int(x) for x in line.strip().split(" ")])
        s += extrapolate(readings)[-1]
print(s)
