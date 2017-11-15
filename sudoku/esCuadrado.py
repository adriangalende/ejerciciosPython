# Comprobamos si la matriz que enviamos es cuadrada

import tests

def esCuadrado(sudoku):

    numeroFilas = len(sudoku)

    for fila in sudoku:

        if len(fila) != numeroFilas:
            return False

    return True


#Casos Test esCuadrado

if __name__ == '__main__':
    for casoTest in list(tests.__dict__.keys()):
        if not casoTest[0] == "_":
            print(casoTest + " :" +  str(tests.__dict__[casoTest]))
            print(esCuadrado(tests.__dict__[casoTest]))
            print("----------------------------")
