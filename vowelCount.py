def getCount(inputStr):
    num_vowels = 0
    vowels = 'aeiou'
    inputStr = inputStr.lower()
    for letter in inputStr:
        if letter in vowels:
            num_vowels += 1

    return num_vowels


#Casos Test
print(getCount("abracadabra"))
#>> 5
