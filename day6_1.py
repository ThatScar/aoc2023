from math import sqrt, ceil, floor

with open("day6.txt") as file:
    times = [int(n) for n in file.readline().strip().split(":")[1].split(" ") if n]
    distances = [int(n) for n in file.readline().strip().split(":")[1].split(" ") if n]

product = 1
for time, target in zip(times, distances):
    # distance > target
    # -hold**2 + time*hold - target > 0
    D = time*time - 4*target
    hold1 = floor((-time + sqrt(D))/-2) + 1
    hold2 = ceil((-time - sqrt(D))/-2) - 1
    print(f"{hold1}:{(time-hold1)*hold1} {hold2}:{(time-hold2)*hold2} > {target}")
    product *= hold2-hold1 + 1
print(product)
