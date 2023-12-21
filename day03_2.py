import re
from dataclasses import dataclass
filename = "day3.txt"

@dataclass
class Number:
    range_i: "range"
    range_j: "range"
    value: int

numbers = []
with open(filename) as file:
    for i, line in enumerate(file):
        line = line.strip()
        ms = re.finditer("\d+", line)
        for m in ms:
            numbers.append(Number(range(i-1,i+2), range(m.start()-1, m.end()+1), int(m.group())))

s = 0
with open(filename) as file:
    for i, line in enumerate(file):
        line = line.strip()
        ms = re.finditer("\*", line)
        for m in ms:
            j = m.start()
            count = 0
            product = 1
            for n in numbers:
                if i in n.range_i and j in n.range_j:
                    count += 1
                    product *= n.value
            if count == 2:
                #print(product)
                s += product
print(s)
