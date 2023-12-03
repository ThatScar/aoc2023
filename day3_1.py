import re
filename = "day3.txt"

coverage = []
with open(filename) as file:
    for i, line in enumerate(file):
        line = line.strip()
        coverage.append([])
        for j, c in enumerate(line.strip()):
            left = coverage[i][j-1] if j > 0 else 0
            above = coverage[i-1][j] if i > 0 else 0
            corner = coverage[i-1][j-1] if j > 0 and i > 0 else 0
            coverage[i].append((c != ".") + left + above - corner)
        coverage[i].append(coverage[i][-1]) #pad right
    coverage.append(coverage[-1]) #pad down

s = 0
with open(filename) as file:
    for i, line in enumerate(file):
        line = line.strip()
        ms = re.finditer("\d+", line)
        for m in ms:
            my_count = coverage[i+1][m.end()]
            left = coverage[i+1][m.start()-2] if m.start() > 1 else 0
            above = coverage[i-2][m.end()] if i > 1 else 0
            corner = coverage[i-2][m.start()-2] if m.start() > 1 and i > 1 else 0
            symbol_count = my_count - left - above + corner
            #print(i, m.start(), m.end(), m.group(), symbol_count)
            #print(my_count, left, above, corner)
            if symbol_count > (m.end()-m.start()):
                s += int(m.group())
print(s)

def print_coverage():
    for line in coverage:
        print("".join([str(min(9,i)) for i in line]))
