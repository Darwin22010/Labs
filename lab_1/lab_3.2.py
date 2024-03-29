import sys

def check_jacob(A):
	n = len(A[0])
	for i in range(n):
		suma = sum(abs(x) for x in A[i]) - abs(A[i][i])
		if abs(A[i][i])<= suma:
			return False
	return True

def seidel(A,b, eps):
	n = len(b)
	x = [0,0]
	x[0] = [b[i] * 1.0 / A[i][i] for i in range(n)]
	x[1] = [0 for _ in range(n)]
	alnorm = max(sum(abs(1.0*A[j][k]/A[j][j]) for k in range(n) if k != j) for j in range(n))
	cnorm = max(sum(abs(1.0*A[j][k]/A[j][j]) for k in range(j+1,n)) for j in range(n))
	coef = (cnorm/(1-alnorm)) if alnorm < 1 else 1
	it = 0
	while True:
		it += 1
		for j in range(n):
			x[it%2][j] = (b[j] - sum(A[j][k]*x[it%2][k] for k in range(j)) - sum(A[j][k]*x[(it+1)%2][k] for k in range(j+1,n))) * 1.0 / A[j][j]
		normx = coef * sum(abs(x[it%2][k]-x[(it+1)%2][k]) for k in range(n))
		if normx <= eps:
			return x[it%2], it

def main():
	print("Matrix A:")
	A = []
	A.append([int(j) for j in input().strip().split(" ")])
	for i in range(1,len(A[0])) :
		A.append([int(j) for j in input().strip().split(" ")])

	print("Vector b:")
	b = [int(j) for j in input().strip().split(" ")]
	
	if not(check_jacob(A)):
		print("Seidel not applicable")
		return
		
	print("Epsilon:")
	eps = float(input())
	
	x, it = seidel(A,b,eps)
	for i in range(len(x)):
		x[i] = (format(x[i], '.4f'))
	print(x)
	print("Number of iterations:")
	print(it)

if __name__ == '__main__':
		main()