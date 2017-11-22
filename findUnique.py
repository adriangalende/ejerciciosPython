
lista=[7, 7, 7, 7, 7, 7, 6, 7,7,7]

def find_uniq(lista):
    #Sabemos que la lista está representada por 2 numeros, uno repetido n veces y otro 1 sola vez
    primerNumero,segundoNumero = set(lista)
    if lista.count(primerNumero) == 1:
        return primerNumero
    else:
        return segundoNumero

print(find_uniq(lista))
