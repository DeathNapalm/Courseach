from math import sqrt
import numpy as np


def seidel(A, b, eps):
    """Разработать программу для численного решения СЛАУ методом Зейделя
    с организацией хранения сильно разреженной матрицы большой размерности"""

    n = len(A)
    x = [.0 for i in range(n)]

    depth = 900
    converge = False
    while not converge :
        depth -=1
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        if depth ==0: break
        converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new

    return x


if __name__ == '__main__':
    print(seidel([[3.6, 1.8, -4.7], [2.7, -3.6, 1.9], [1.5, 4.5, 3.3]], [3.8, 0.4, -1.6], 0.001))
    print(seidel([[3.6, 2.7, 1.5], [1.8, -3.6, 4.5], [-4.7, 1.9, 3.3]], [3.8, 0.4, -1.6], 0.001))
    print(seidel([[3.6, 1.8, -4.7, 3.8], [2.7, -3.6, 1.9, 0.4], [1.5, 4.5, 3.3,-1.6]], [3.8, 0.4, -1.6], 0.001))