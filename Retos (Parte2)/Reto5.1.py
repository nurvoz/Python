'''
El Sudoku es un popular pasatiempo que tenéis definido en https://es.wikipedia.org/wiki/Sudoku

Te pedimos que realices una función que reciba un array bidimensional con un Sudoku de 9x9 resuelto

y devuelva true si el Sudoku es correcto, false en caso contrario.

La función debe definirse con este estilo:

def esSudokuCorrecto(miSudoku)
'''
def esSudokuCorrecto(miSudoku):
    # Verificar filas y columnas
    for i in range(9):
        if len(set(miSudoku[i])) != 9 or len(set(miSudoku[j][i] for j in range(9))) != 9:
            return False

    # Verificar subcuadrículas de 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if len(set(miSudoku[x][y] for x in range(i, i+3) for y in range(j, j+3))) != 9:
                return False

    return True

# Ejemplo de uso
sudoku_correcto = [
    [4, 1, 3, 8, 2, 5, 6, 7, 9],
    [5, 6, 7, 1, 4, 9, 8, 3, 2],
    [2, 8, 9, 7, 3, 6, 1, 4, 5],
    [1, 9, 5, 4, 6, 2, 7, 8, 3],
    [7, 2, 6, 9, 8, 3, 5, 1, 4],
    [3, 4, 8, 5, 1, 7, 2, 9, 6],
    [8, 5, 1, 6, 9, 4, 3, 2, 7],
    [9, 7, 2, 3, 5, 8, 4, 6, 1],
    [6, 3, 4, 2, 7, 1, 9, 5, 8]
]

print(esSudokuCorrecto(sudoku_correcto))  # True