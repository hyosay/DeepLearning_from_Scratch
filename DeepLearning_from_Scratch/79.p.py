def adjacent(inputArray):
    sum1 = sum1()

    for i in range(0, 9):
        sum1.append(inputArray[i] * inputArray[i + 1])
    print(sum1)
inputArray = [1,2,3,4,5,6,7,8,9,10]
adjacent(inputArray)
