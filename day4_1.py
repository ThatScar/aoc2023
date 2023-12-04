s = 0
with open("day4.txt") as file:
    for line in file:
        _, numbers = line.strip().split(":")
        win, have = numbers.strip().split("|")
        win_set = set(int(n) for n in win.split(" ") if n)
        have_set = set(int(n) for n in have.split(" ") if n)
        intersection = win_set & have_set
        score = 2**len(intersection) // 2
        print(score, intersection)
        s += score
print(s)
