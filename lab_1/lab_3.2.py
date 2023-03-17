A = [
[24,2,4,-9],
[-6,-27,-8,-6],
[-4,8,19,6],
[4,5,-3,-13]]
B = [-9,-76,-79,-70]
 
# точность итераций
c = 4
eps = 1/10**c
x = []
n = len(A)
for j in range(n):
    k = A[j][j]
    for i in range(n):
        A[j][i] /= -k 
    A[j][j] = 0
    B[j] /= k 
 
# r - счетчик итераций
r = 0
x = B.copy()
tmp = sum(x) + 2*eps
while abs(sum(x)-tmp) > eps:
    tmp = sum(x)
    t = [0]*n
    for i in range(n):
        t[i] = sum(x[j]*A[i][j] for j in range(n)) + B[i]
    r += 1
    x = t.copy()
print(*(round(elem,3) for elem in x))
print(r)