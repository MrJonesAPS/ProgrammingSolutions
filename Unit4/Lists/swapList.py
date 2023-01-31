def swapList(myList):
    #complete this function
    x = 0

    while x+1 < len(myList):
        first = myList[x]
        second = myList[x+1]

        myList[x] = second
        myList[x+1] = first

        x += 2

    return myList