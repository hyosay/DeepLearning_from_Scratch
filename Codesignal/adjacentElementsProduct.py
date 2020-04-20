def adjacentElementsProduct(inputArray):

    length = len(inputArray)

    sum = []

    for i in range(length - 1):

        sum.append(inputArray[i] * inputArray[i + 1])
    print(max(sum))
inputArray = [5, 1, 2, 3, 1, 4]
adjacentElementsProduct(inputArray)