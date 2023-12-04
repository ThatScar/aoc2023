s = 0
own = []
with open("day4.txt") as file:
    for i, line in enumerate(file):
        _, numbers = line.strip().split(":")
        win, have = numbers.strip().split("|")
        win_set = set(int(n) for n in win.split(" ") if n)
        have_set = set(int(n) for n in have.split(" ") if n)
        intersection = win_set & have_set
        if len(own) <= i:
            own.append(1)
        for j in range(len(intersection)):
            if len(own) <= i+j+1:
                own.append(1)
            own[i+j+1] += own[i]
        print(own[i])
        s += own[i]
print(s)
