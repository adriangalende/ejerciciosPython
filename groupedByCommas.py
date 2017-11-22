def group_by_commas(n):
    posicion = 0
    resultado = ""
    for numero in (str(n))[::-1]:
        if posicion%3 == 0 and posicion != 0:
            resultado += ',' + numero
        else:
            resultado += numero

        posicion += 1

    return resultado[::-1]


print(group_by_commas(1000))
