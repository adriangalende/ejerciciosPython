lista = [1,2,3,2,4,5,1,2,3]

def productoNumeros(numeroUnico):
  resultado = 1
  for numero in numeroUnico:
    resultado *= numero
  return resultado


def imprimirListaNumeros(lista,numeroAIgnorar):
  numeroUnico = []
  for numero in lista:
    if numero not in numeroAIgnorar:
      numeroUnico.append(numero)
  #return productoNumeros(numeroUnico) para que devuelva el productoNumeros
  return numeroUnico


def numeroUnico(lista):
  i = 0
  numeroAIgnorar = []
  for numero in lista:
    if numero in lista[i+1:]:
      numeroAIgnorar.append(numero)
    i += 1
  return imprimirListaNumeros(lista,numeroAIgnorar)




print(numeroUnico(lista))
