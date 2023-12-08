with open("day5.txt") as file:
    numbers = [int(x) for x in file.readline().strip().split(": ")[1].split(" ")]
    file.readline()
    while line:= file.readline().strip():
        print(numbers)
        assert(line in ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"])
        new_numbers = numbers[::]
        for line in file:
            line = line.strip()
            if not line:
                break
            destination, source, length = (int(x) for x in line.split(" "))
            for i, number in enumerate(numbers):
                offset = number - source
                if 0 <= offset < length:
                    #print(f"{i} {destination + offset}<={number} {destination}<={source} {length}")
                    new_numbers[i] = destination + offset
        numbers = new_numbers
print(numbers)
print(min(numbers))
