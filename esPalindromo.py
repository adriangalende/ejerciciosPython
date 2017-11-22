#sin recursividad
'''def esPalindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False

'''
# Con recursividad
def esPalindromo(palabra):
    if palabra == "":
        return True
    else:
        if palabra[0] == palabra[-1]:
            return esPalindromo(palabra[1:-1])
        else:
            return False
print(esPalindromo("amanaplanacanalpanama"))




#Test
#esPalindromo("a")
#>> True
#esPalindromo("")
#>> True
#esPalindromo("level")
#>>True
#esPalindromo("ojo")
#>>True
#esPalindromo("agua")
#>> False
