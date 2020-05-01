N = 3
a = [ [None] * N for i in range(N)]

c = []
for q in range(N * N):
    c.append(q)
for z in range(9):
    for i in range(N):
        for j in range(N):
            a[i][j] = c[z]


total = 0
for k in range(N):
    for l in range(N):
        if k == l:
            total = total + a[k][l]
print(total)