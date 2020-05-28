N = 3
a = [[None] * N for i in range(N)]

for i in range(N):
    for j in range(N):
        a[i][j] = float(input())

total = 0
for k in range(N):
    total = total + a[k][k]

print("총합", total)