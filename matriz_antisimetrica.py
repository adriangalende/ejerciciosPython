# Define una rutina que devuelve True si una matriz es
# atisimetrica y False en otro caso.
# Una matriz n*n es antisimetrica si se verifica que
# sus elementos mantienen la relación:
# matriz[i][j] = - matriz[j][i]
# para cada i=0,1,...,n-1 y para cada j=0,1,...,n-1.


# matriz = [[lista][lista][lista]]
#Comprobamos que en números de elementos en la matriz (filas) es igual
# al numero de elementos en cada lista ( columnas )
def esMatrizCuadrada(matriz):
    numeroFilas = len(matriz)
    for fila in matriz:
        if len(fila) != numeroFilas:
            return False
    return True

def esAntisimetrica(matriz):
    # Comprobamos que la matriz que vamos a analizar sea cuadrada
    if esMatrizCuadrada(matriz):
        i = 0 #Filas
        j = 0 #Columnas

        while i <= len(matriz)-1:
            while j <= len(matriz[i])-1:
                # Si matriz[fila][columnas] es diferente
                if matriz[i][j] != -matriz[j][i]:
                    return False
                j += 1
            i += 1
        return True
    else:
        # La matriz no es cuadrada
        return False



# Casos Test:

print(esAntisimetrica([[0, 4, 2],
                     [-1, 0, 3],
                     [-2, -3, 0]]))
