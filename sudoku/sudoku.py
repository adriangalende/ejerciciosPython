# encoding: utf-8

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

import tests,esCuadrado as matriz ,checkeoNumeros,filas,columnas

def check_sudoku(sudoku):

    return matriz.esCuadrado(sudoku) and checkeoNumeros.checkNumerosValidos(sudoku) and filas.checkFilas(sudoku) and columnas.checkColumnas(sudoku)


## Casos test ##

if __name__ == '__main__':
    for casoTest in list(tests.__dict__.keys()):
        if not casoTest[0] == "_":
            print(casoTest + " :" +  str(tests.__dict__[casoTest]))
            print(check_sudoku(tests.__dict__[casoTest]))
            print("----------------------------")
