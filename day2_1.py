s = 0
with open("day2.txt") as file:
    for line in file:
        game, reads = line.strip().split(": ")
        valid = True
        for read in reads.split("; "):
            for aggregate in read.split(", "):
                count, colour = aggregate.split(" ")
                count = int(count)
                if colour == "red" and count > 12\
                   or colour == "green" and count > 13\
                   or colour == "blue" and count > 14:
                    valid = False
        print(f"{game}: {valid}")
        if valid:
            _, i = game.split(" ")
            s += int(i)
print(s)
