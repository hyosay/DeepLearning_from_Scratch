#1
'''def shapeArean(n):
    max = 0
    for i in range(1,n + 1):
        max += (i * 2 - 1)
    for i in  range(n -1, 0, -1):
        max += (i * 2 - 1)

    print(max)'''


#2
def shapeArean(n):
    return(pow(n,2) + pow(n-1, 2)) #pow = 제곱근