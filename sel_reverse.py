#

def sel_reverse(lista,longitud):

    if longitud == 0:
        return lista

    if len(lista) < longitud:
        return lista[::-1]

    i = 0
    listaOrdenada = []
    listaComodin = []
    while i <= len(lista)-1:
        listaComodin = lista[i:i+longitud]
        listaOrdenada.extend(listaComodin[::-1])
        listaComodin = []
        i += longitud
        if longitud/2 == 0:
            i -= 1
    return listaOrdenada


###Test###

#selReverse([1,2,3,4],2)
#>> [2,1,4,3]

#selReverse([1,2,3,4,5,6], 2)
#>> [2,1, 4,3, 6,5]

#selReverse([2,4,6,8,10,12,14,16], 3)
#>> [6,4,2, 12,10,8, 16,14]
