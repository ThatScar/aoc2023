from math import sqrt, ceil, floor

with open("day6.txt") as file:
    time = int(file.readline().strip().split(":")[1].replace(" ", ""))
    target = int(file.readline().strip().split(":")[1].replace(" ", ""))

print(time, target)
# distance > target
# -hold**2 + time*hold - target > 0
D = time*time - 4*target
hold1 = floor((-time + sqrt(D))/-2) + 1
hold2 = ceil((-time - sqrt(D))/-2) - 1
print(f"{hold1}:{(time-hold1)*hold1} {hold2}:{(time-hold2)*hold2} > {target}")
print(hold2-hold1 + 1)

