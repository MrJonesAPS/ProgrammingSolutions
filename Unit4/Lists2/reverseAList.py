def reverseAList(myList):
    reversedList = []

    i = -1 

    while i >= -1*len(myList): 

        reversedList.append(myList[i])

        i = i - 1

    return reversedList


testList = [1,2,3]
print(reverseAList(testList))