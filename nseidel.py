import numpy as np
import sys

ITERATION_LIMIT = 100000
n = int(input('Ведите количество уравнений: '))

a =[]
#print(a)
b = []
e = float(input('Введите точность'))*10e-22
#rounding = len(e)-1

#n = int(input('Ведите количество уравнений: '))
for row in range(n):
    #for column in range(n):
    #aa = float(input('введите а[{}][{}]: '.format(row, 1)))
    a.append(list(map(float, input().split())))
##a = np.loadtxt(sys.stdin)
for i in range(n):
    bb = float(input('введите b[{}]: '.format(i)))
    b.append(bb)

# initialize the matrix
A = np.array(a)
# initialize the RHS vector
b = np.array(b)

# A = np.array([[3.6, 1.8, -4.7],
#               [2.7, -3.6, 1.9],
#               [1.5, 4.5, 3.3]])
# # initialize the RHS vector
# b = np.array([3.8, 0.4, -1.6])
print(A,b, sep='/n')

if np.linalg.det(a) ==0:
    print('Матрица вырожденная, будет выведен один из возможных ответов')
else : print("Матрица невырожденная")

print("Система уравнений:")
for i in range(A.shape[0]):
    row = ["{0:3g}*x{1}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))

A = np.dot(np.transpose(a),a)
b = np.dot(np.transpose(a),b)


x = np.zeros_like(b)
for it_count in range(1, ITERATION_LIMIT):
    x_new = np.zeros_like(x)
    print("Итерация {0}: {1}".format(it_count, x))
    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = ((b[i] - s1 - s2) / A[i, i])
    if np.allclose(x, x_new, atol=e):
        break
    x = x_new

print("Решение: {0}".format(x))
error = np.dot(A, x) - b
print("Погрешность: {0}".format(error))