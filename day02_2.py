s = 0
with open("day2.txt") as file:
    for line in file:
        game, reads = line.strip().split(": ")
        lowest_counts = dict()
        for read in reads.split("; "):
            for aggregate in read.split(", "):
                count, colour = aggregate.split(" ")
                count = int(count)
                lowest_counts[colour] = max(count, lowest_counts.get(colour,0))
        print(lowest_counts)
        power = lowest_counts["red"] * lowest_counts["green"] * lowest_counts["blue"]
        s += power
print(s)
