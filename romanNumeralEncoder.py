
#En el enunciado dice que no pueden haber más de 2 valores repetidos en la misma fila,
# pero en el caso de que numero > 2999 se deberá añadir una M en los miles...
import random


equivalenciasNumRomanos = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def convertirARomano(numero):

    if numero <= 0: return ""

    numeroRomano = ""
    #recorremos la lista de tuplas una a una
    for valor, letra in equivalenciasNumRomanos:
        #encuentra una tupla que contiene un numero menor o igual al numero recibido por parametro
        while numero >= valor:
            numeroRomano += letra
            #como hemos encontrado un valor menor o igual al numero de la tupla
            numero -= valor

    return numeroRomano


numero = random.randint(1,2999)
print(numero)
print(convertirARomano(numero))
#casos Test
#convertirARomano(0)
#>>
#convertirARomano(1)
#>> I
#convertirARomano(2)
#>> II
#convertirARomano(8)
#>> VIII
#convertirARomano(555)
#>> DLV
#convertirARomano(1999)
#>> MCMXCIX
#convertirARomano(2017)
#>> MMXVII
