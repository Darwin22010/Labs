from lab_1 import *
M = [[10, 5, 0, 0, 0], [3, 10, -2, 0, 0], [0, 2, -9, -5, 0], [0, 0, 5, 16, -4], [0, 0, 0, -8, 16]]
D = [-120, -91, 5, -74, -56]
n = 4
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
        if abs(B[i]) < abs(A[i]) + abs(C[i]):
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
    print('Значения P')
    for i in range(n):
        print("%.1f" % P[i], end = " ")
    print()
    print('Значения Q')
    for i in range(n):
        print("%.1f" % Q[i], end = " ")
    print()
    print('Значения X')
    for i in range(n):
        print("%.1f" % X[i], end = " ")

progonka_matrix(M, D)