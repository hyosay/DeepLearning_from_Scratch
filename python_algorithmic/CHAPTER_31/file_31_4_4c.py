import math
ELEMENTS = 5

values = []
for i in range(ELEMENTS):
    values.append(int(input()))

total = math.fsum(values)
print(total)