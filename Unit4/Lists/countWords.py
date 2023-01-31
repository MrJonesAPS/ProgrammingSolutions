def countWords(myList):
    #complete this function
    numFiveLetterWords = 0
    for i in myList:
        if len(i) == 5:
            numFiveLetterWords = numFiveLetterWords + 1

    return numFiveLetterWords