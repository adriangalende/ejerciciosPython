
#vowels = a e i o u y

def vowel_indices(word):
    word = word.lower()
    position = []
    index = 1
    vowels = 'aeiouy'
    for letter in word:
        if letter in vowels:
            position.append(index)

        index += 1
    return position





#casos Test
print(vowel_indices('YoMama'))
#vowel_indices('Super') ==> [2,4]
#vowel_indices('Apple') ==> [1,5]
#vowel_indices('YoMama') ==> [1,2,4,6]
