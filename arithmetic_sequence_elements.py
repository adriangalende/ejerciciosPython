

def arithmetic_sequence_elements(a, r, n):
    result = str(a)+", "
    sumando = a
    for i in range(n-1):
        sumando += r
        result += str(sumando)
        if i < n:
            result += ', '
    return result[:-2]



print(arithmetic_sequence_elements(-1, 2, 5))

# Casos Test

# arithmetic_sequence_elements(1, 2, 5)
# >> '1, 3, 5, 7, 9'
# arithmetic_sequence_elements(-1, 2, 5)
# >> '-1, 1, 3, 5, 7'
#arithmetic_sequence_elements(1, -3, 10)
#>> '1, -2, -5, -8, -11, -14, -17, -20, -23, -26'
#arithmetic_sequence_elements(2, -3, 10)
#>> '2, -1, -4, -7, -10, -13, -16, -19, -22, -25'
