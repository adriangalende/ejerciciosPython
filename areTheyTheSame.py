
def comp(a,b):

    if a == None or b == None:
        return False

    listaCuadrados = []
    for numero in a:
        listaCuadrados.append(numero**2)

    listaCuadrados.sort()

    b.sort()

    return listaCuadrados == b

a = []
b = []

print(comp(a,b))
