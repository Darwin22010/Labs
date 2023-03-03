import numpy as np
import math 

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

def decompose_to_LU(matrix):
    """Разложить матрицу коэффициентов на матрицы L и U.
      Треугольные матрицы L и U будут представлены одной матрицей размера nxn.
     :param a: numpy матрица коэффициентов
     :return: пустая матрица LU
    """
    # create emtpy LU-matrix
    lu_matrix = []
    for i in range(n):          
        a = []
        for j in range(n):      
          a.append(0)
        lu_matrix.append(a)

    for k in range(n):
        # calculate all residual k-row elements
        for j in range(k, n):
            lu_matrix[k][j] = matrix[k][j] - lu_matrix[k][k] * lu_matrix[k][j]
        # calculate all residual k-column elemetns
        for i in range(k + 1, n):
            lu_matrix[i][k] = (matrix[i][k] - lu_matrix[i][k] * lu_matrix[k][k]) / lu_matrix[k][k]

    return lu_matrix

n = int(input("Введите размерность матриц:"))
