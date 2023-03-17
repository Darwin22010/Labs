import numpy as np

def matrix_creat():
    matrix = []
    print(f"Введите матрицу размерности {n} по строчно и по символьно")
    for i in range(n):          
        a =[]
        for j in range(n):      
          a.append(int(input()))
        matrix.append(a)
    return(matrix)

def vector_creat():
    print(f"Введите вектор длины {n} по строчно и по символьно")
    vector = []
    for i in range(n):
        vector.append(int(input()))
    return(vector)

def matrix_print(matrix):
    for i in range(n):
        for j in range(n):
            print("%.0f" % matrix[i][j], end = " ")
        print()
    return

def vector_print(vector):
    for i in range(n):
            print("%.0f" % vector[i], end = " ")
            print()
    return

def multiplication_matrix(matrix1, matrix2):
    R = []
    for i in range(n):          
        a =[]
        for j in range(n):      
          a.append(0)
        R.append(a)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                R[i][j] += matrix1[i][k] * matrix2[k][j]
    return R

def multiplication_vector(matrix1, vector):
    R = []
    for i in range(n):               
          R.append(0)
    for i in range(n):
            for k in range(n):
                R[i] += matrix1[i][k] * vector[k]
    return R

def determination_matrix(matrix):
    det = np.linalg.det(matrix)
    return det

def inversion_matrix(matrix):
    inverse_matrix = np.linalg.inv(matrix)
    return inverse_matrix

n = int(input("Введите размерность матриц:"))

matrix = np.array([[3.8, 6.7, -1.2, 5.2], 
                   [6.4, 1.3, -2.7, 3.8], 
                   [2.4, -4.5, 3.5, -0.6]])
def make_identity(matrix):
    # перебор строк в обратном порядке
    for nrow in range(len(matrix)-1,0,-1):
        row = matrix[nrow]
        for upper_row in matrix[:nrow]:
            factor = upper_row[nrow]
            upper_row -= factor*row
    return matrix

def gaussPivotFunc(matrix):
    for nrow in range(len(matrix)):
        # nrow равен номеру строки
        # np.argmax возвращает номер строки с максимальным элементом в уменьшенной матрице
        # которая начинается со строки nrow. Поэтому нужно прибавить nrow к результату
        pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
        if pivot != nrow:
            # swap
            # matrix[nrow], matrix[pivot] = matrix[pivot], matrix[nrow] - не работает.
            # нужно переставлять строки именно так, как написано ниже
            matrix[[nrow, pivot]] = matrix[[pivot, nrow]]
        row = matrix[nrow]
        divider = row[nrow] # диагональный элемент
        if abs(divider) < 1e-10:
            # почти нуль на диагонали. Продолжать не имеет смысла, результат счёта неустойчив
            raise ValueError(f"Матрица несовместна. Максимальный элемент в столбце {nrow}: {divider:.3g}")
        # делим на диагональный элемент.
        row /= divider
        # теперь надо вычесть приведённую строку из всех нижележащих строчек
        for lower_row in matrix[nrow+1:]:
            factor = lower_row[nrow] # элемент строки в колонке nrow
            lower_row -= factor*row # вычитаем, чтобы получить ноль в колонке nrow
    # приводим к диагональному виду
    make_identity(matrix)
    return matrix
print(gaussPivotFunc(matrix))
