def caesar_one_letter(letter_to_encrypt, number_to_add):
    NumberOfCapitalA = 65
    letterAsNumber = ord(letter_to_encrypt) - NumberOfCapitalA
    newLetterAsNumber = (letterAsNumber + number_to_add) % 26
    encryptedLetter = chr(newLetterAsNumber + NumberOfCapitalA)
    return encryptedLetter


def caesar_string(string_to_encrypt, number_to_add):
    
    encryptedString = ""
    i = 0
    while i < len(string_to_encrypt):
        if string_to_encrypt[i] == " ":
            encryptedString += " "
        else: 
            encryptedString += caesar_one_letter(string_to_encrypt[i], number_to_add)
        i = i + 1

    #TODO: Complete this function

    return encryptedString



#Here's some code that you can use to test caesar_string
testString = "SDKKZKKXNTQEQHDMCRSNSZJDOQNFQZLLHMFMDWSXDZQ"
print(caesar_string(testString, 1))