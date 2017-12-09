def matrix(alem,jptr,iptr,i,j):
    """получить элемент из матрицы """

    res = 0
    n1 = iptr[i]
    n2 = iptr[i+1]
    for k in range(n1,n2):
        if jptr[k] == j:
            res = alem[k]
            break
    return res


def seidel(alem, jptr, iptr, eps):
    """Разработать программу для численного решения СЛАУ методом Зейделя
    с организацией хранения сильно разреженной матрицы большой размерности"""

    n = len(iptr-1)
    previousVariableValues = [.0 for i in range(n)]

    while True:
        currentVariableValues = [0]*n
        for i in range(n):
            currentVariableValues[i] = matrix(alem, jptr, iptr, i, n); # можно совместить с генератором
            for j in range(n):
                if j < i:
                    currentVariableValues[i] -= matrix(alem, jptr, iptr, i, j) * currentVariableValues[j]
                if (j > i):
                    currentVariableValues[i] -= matrix(alem, jptr, iptr, i, j) * previousVariableValues[j]

            currentVariableValues[i] /= matrix(alem, jptr, iptr, i, j)
        error = 0.0

        for i in range(n):
            error += abs(currentVariableValues[i] - previousVariableValues[i])
            if error < eps:
                break
            previousVariableValues = currentVariableValues


    return previousVariableValues

if __name__ == '__main__':
    print(seidel())