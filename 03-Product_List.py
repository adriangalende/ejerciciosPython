# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(lista):
    result = 1
    for num in lista:
        result *= num
    return result

print(product_list([1,2,3,4]))

#print product_list([9])
#>>> 9

#print product_list([1,2,3,4])
#>>> 24

#print product_list([])
#>>> 1
