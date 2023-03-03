from lab_1 import *
M = matrix_creat()
D = vector_creat()

def progonka_matrix(matrix, vector):
    Q = []
    P = []
    X = []
    A = [0]
    B = []
    C = []
    for i in range(n):
        Q.append(0)
        P.append(0)
        X.append(0)
        if i != n-1:
            A.append(matrix[i+1][i])
            B.append(matrix[i][i])
            C.append(matrix[i][i+1])
        else:
            B.append(matrix[i][i])
            C.append(0)
    for i in range(n):
        if abs(B[i]) < abs(A[i]):
            print('достаточное условие не выполняется')
            quit()
    P[0] = -C[0] / B[0]
    Q[0] = vector[0] / B[0]
    for i in range(1,n):
        P[i] = -C[i] / (B[i] + A[i] * P[i-1])
        Q[i] = (vector[i] - A[i] * Q[i-1]) / (B[i] + A[i] * P[i-1])
    v = n - 1
    X[v] = Q[v]
    while v != 0:
        v -= 1
        X[v] = P[v] * X[v+1] + Q[v]
    return X

print(progonka_matrix(M, D))