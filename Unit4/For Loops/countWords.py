def countWords(myList):
    fives = 0
    for w in myList:
        if len(w) == 5:
            fives += 1

    return fives