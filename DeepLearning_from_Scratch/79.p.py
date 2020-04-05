years = int(input())

if years % 4 == 0:
    if years % 100 != 0:
        print(1)
    elif years % 400 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)
