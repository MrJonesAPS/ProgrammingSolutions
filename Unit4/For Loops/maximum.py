def maximum(myList):
    #complete this function
    highest = myList[0]
    for num in myList:
        if num > highest:
            highest = num
    return highest
