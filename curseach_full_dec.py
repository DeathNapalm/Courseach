from math import sqrt
from copy import deepcopy
#from numpy import copy
from decimal import *
getcontext().prec = 5

def input_into_scr():     #massiv strok
    """Ввод матрицы с клавиатуры с параллельным переводом в сжатый формат"""
    eps = Decimal(input('Введите точность: '))
    n = int(input('введите количество строк: '))
    aelem = []  #j  sto]bec, i stroka
    jptr = []
    iptr = [0]
    current_row = 0
    counter = 0
    for row in range(n):
        for column in range(n+1):
            a = Decimal(input('введите а[{}][{}]: '.format(row,column)))
            if row != current_row:
                iptr.append(counter)
                current_row = row
            if a != 0:
                aelem.append(a)
                counter += 1
                jptr.append(column)

    iptr.append(counter)
    return aelem, jptr, iptr, eps


def matrix(aelem, jptr, iptr, i, j):
    """Интерфейс получения элемента по его индексам из сжатой матрицы"""
    res = Decimal(0.0)
    n1 = iptr[i]
    n2 = iptr[i+1]
    for k in range(n1,n2):
        if jptr[k] == j:
            res = aelem[k]
            break
    return res


def seidel(aelem, jptr, iptr, eps):
    """Разработать программу для численного решения СЛАУ методом Зейделя
    с организацией хранения сильно разреженной матрицы большой размерности"""

    n = len(iptr)-1
    x = [Decimal(0.0) for i in range(n)]
    converge = False

    while not converge:
        x_new = deepcopy(x)
        for i in range(n):
            s1 = Decimal(sum(matrix(aelem, jptr, iptr,i, j) * x_new[j] for j in range(i)))
            s2 = Decimal(sum(matrix(aelem, jptr, iptr,i, j) * x[j] for j in range(i + 1, n)))
            x_new[i] = Decimal((matrix(aelem, jptr, iptr, i, n)) - s1 - s2) / Decimal(matrix(aelem, jptr, iptr,i, i))
        converge_cond = Decimal((sum((x_new[i] - x[i]) ** 2 for i in range(n)))).sqrt()
        converge = converge_cond <=eps
        x = x_new

    return x


if __name__ == '__main__':
    # print(seidel([[3.6, 1.8, -4.7], [2.7, -3.6, 1.9], [1.5, 4.5, 3.3]], [3.8, 0.4, -1.6], 0.001))
    # print(seidel([[3.6, 2.7, 1.5], [1.8, -3.6, 4.5], [-4.7, 1.9, 3.3]], [3.8, 0.4, -1.6], 0.001))
    #print(seidel([3.6, 1.8, -4.7, 3.8, 2.7, -3.6, 1.9, 0.4, 1.5, 4.5, 3.3, -1.6], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], [0, 4, 8, 12], 0.001))
    #print(seidel([[0.945, -0.5882, 0, 0, 0], [-0.017, 0.9806, -0.0114, 0, 0], [0, -0.0153, 0.9876, -0.0107, 0], [0, 0, -0.1111, 0.9188, -0.5], [0, 0, 0, -0.75, 0.9378]], [50,-15.2371,-14.2308,0,-48], 0.0001))
    #[43.5987285945029, -14.959540119074564, -15.21082815402478, -52.57321995394093, -93.2287427654678]
    #print(seidel([0.945, -0.5882, 50.0, -0.017, 0.9806, -0.0114, -15.2371, -0.0153, 0.9876, -0.0107, -14.2308, -0.1111, 0.9188, -0.5, -0.75, 0.9378, -48.0], [0, 1, 5, 0, 1, 2, 5, 1, 2, 3, 5, 2, 3, 4, 3, 4, 5], [0, 3, 7, 11, 14, 17], 0.0001))
    aelem, jptr, iptr, eps = input_into_scr()
    print(seidel(aelem, jptr, iptr, eps))