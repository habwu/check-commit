n = int(input())
diameters = [0] * 101 
for _ in range(n):
    diameter = int(input())
    diameters[diameter - 600] += 1

wagons = 0
for count in diameters:
    wagons += count // 4

print(wagons)
