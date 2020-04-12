total = 0

i = 1
while i <= 5:
    a = int(input())
    if a % 2 != 0:
        total = total + a
    i += 1
print(total)