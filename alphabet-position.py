'''
def alphabet_position(text):
    alphabet = ( 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' )
    index = ""
    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i].lower() == alphabet[j]:
                index = index + str(j+1) + " "
                break

    return index.strip()
'''

def alphabet_position(text):
    FIRSTASCIIPOSITION = 96
    result = ""
    for letter in text.lower():
      if str(letter).isalpha():
          result += str(ord(letter) - FIRSTASCIIPOSITION) + " "
    return result.strip()



#Casos test
#print(alphabet_position("The sunset sets at twelve o' clock."))
#>>
#print(alphabet_position("The narwhal bacons at midnight."))

#print(alphabet_position(""))
