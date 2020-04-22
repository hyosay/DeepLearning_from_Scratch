def adjacentElementsProduct(inputArray):

    length = len(inputArray)

    sum = []

    for i in range(length - 1):

        sum.append(inputArray[i] * inputArray[i + 1]) # append = added to the list
    print(max(sum))

inputArray = [3, 6, -2, -5, 7, 3]
adjacentElementsProduct(inputArray)