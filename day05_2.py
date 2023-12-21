from dataclasses import dataclass
@dataclass
class row:
    destination: int
    source: int
    length: int

    def as_tuple(self):
        return (self.destination, self.source, self.length)

    def __lt__(self, other):
        return self.as_tuple() < other.as_tuple()

seeds = []

mappings = []
with open("day5.txt") as file:
    numbers = [int(x) for x in file.readline().strip().split(": ")[1].split(" ")]
    for i in range(len(numbers)//2):
        seeds.append((numbers[i*2], numbers[i*2] + numbers[i*2+1]))
    file.readline()
    while line:= file.readline().strip():
        assert(line in ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"])
        mapping = []
        for line in file:
            line = line.strip()
            if not line:
                break
            mapping.append(row(*tuple(int(x) for x in line.split(" "))))
        mapping = sorted(mapping)
        mappings.append(mapping)

print(seeds)

def delve(depth, left, right):
    #print(depth, left, right)
    if left >= right:
        #print("bah")
        return -1
    if depth > len(mappings):
        for seed_row in seeds:
            if seed_row[0] < right and left < seed_row[1]:
                number = max(left, seed_row[0])
                print("found", number)
                return number
        #print("not found")
        return -1
    mapping = iter(mappings[-depth])
    answer = -1
    for r in mapping:
        #print(r)
        if r.destination + r.length > left:
            #left of r
            answer = delve(depth+1, left, min(right, r.destination))
            if answer != -1:
                break
            #r
            offset = r.destination - r.source
            answer = delve(depth+1, max(left, r.destination) - offset, min(right, r.destination + r.length) - offset)
            if answer != -1:
                answer += offset
                break
            left = r.destination + r.length
    #right of r
    if answer == -1:
        answer = delve(depth+1, left, right)
    if answer != -1:
        print(f"got {answer} at depth {depth}")
    return answer

print(delve(0, 0, 1e12))
