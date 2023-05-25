import numpy as np


def qr_eigen(matrix, eps, max_iterations):

    n = matrix.shape[0]
    Q = np.identity(n)

    for _ in range(max_iterations):
        Q_new, R = np.linalg.qr(matrix @ Q)
        if np.allclose(Q, Q_new, atol=eps):
            break
        Q = Q_new

    eigenvalues = np.diag(R)

    while np.iscomplex(eigenvalues).any():
        for i in range(n):
            if np.iscomplex(eigenvalues[i]):
                shift = eigenvalues[i]
                shifted_matrix = matrix - shift * np.identity(n)
                Q, R = np.linalg.qr(shifted_matrix)
                eigenvalues[i] = R[i, i] + shift

        Q_new, R = np.linalg.qr(matrix @ Q)
        if np.allclose(Q, Q_new, atol=eps):
            break
        Q = Q_new
        eigenvalues = np.diag(R)

    return eigenvalues

def find_eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    eigen_pairs = [(eigenvalues[i], eigenvectors[:, i]) for i in range(matrix.shape[0])]
    return eigen_pairs


matrix = np.array([[-6, -4, 0], [-7, 6, -7], [-2, -6, -7]])
eps = 0.01
max_iterations = 1000
eigen_pairs = find_eigen(matrix)
print('Собственные значения:')
for eigenvalue, eigenvector in eigen_pairs:
    print(eigenvalue)
