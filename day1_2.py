import re
sum = 0
with open("day1.txt") as file:
    for line in file:
        line = line.strip()\
                .replace("one", "o1ne")\
                .replace("two", "t2wo")\
                .replace("three", "t3hree")\
                .replace("four", "f4our")\
                .replace("five", "f5ive")\
                .replace("six", "s6ix")\
                .replace("seven", "s7even")\
                .replace("eight", "e8ight")\
                .replace("nine", "n9ine")
                #zero is not a digit???
        line = re.sub(r"^[a-z]*", "", line)
        line = re.sub(r"[a-z]*$", "", line)
        #print(line)
        sum += int(line[0])*10 + int(line[-1])
print(sum)
