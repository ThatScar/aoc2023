import re
sum = 0
with open("day1.txt") as file:
    for line in file:
        line = re.sub(r"^[a-z]*", "", line.strip())
        line = re.sub(r"[a-z]*$", "", line)
        #print(line)
        sum += int(line[0])*10 + int(line[-1])
print(sum)
