import tests

def sonNumerosEnteros(sudoku):

    for fila in sudoku:

        for numero in fila:

            if not isinstance(numero, int):
                return False

    return True

def numerosEnRango(sudoku):

    numerosValidos = range(1, len(sudoku) + 1)

    for fila in sudoku:

        for numero in fila:

            if numero not in numerosValidos:
                return False

    return True

def checkNumerosValidos(sudoku):
    return sonNumerosEnteros(sudoku) and numerosEnRango(sudoku)

## Casos test ##

if __name__ == '__main__':
    for casoTest in list(tests.__dict__.keys()):
        if not casoTest[0] == "_":
            print(casoTest + " :" +  str(tests.__dict__[casoTest]))
            print(checkNumerosValidos(tests.__dict__[casoTest]))
            print("----------------------------")
