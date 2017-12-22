from math import sqrt
from copy import deepcopy
#from numpy import copy


def input_into_scr():     #massiv strok
    """Ввод матрицы с клавиатуры с параллельным переводом в сжатый формат"""
    eps = float(input('Введите точность: '))
    n = int(input('введите количество строк: '))
    aelem = []  #j  sto]bec, i stroka
    jptr = []
    iptr = [0]
    current_row = 0
    counter = 0
    b = []
    for row in range(n):
        for column in range(n):
            a = float(input('введите а[{}][{}]: '.format(row,column)))
            if row != current_row:
                iptr.append(counter)
                current_row = row
            if a != 0:
                aelem.append(a)
                counter += 1
                jptr.append(column)
    for i in range(n):
        a = float(input('введите b[{}]: '.format(i)))
        b.append(a)
    iptr.append(counter)
    return aelem, jptr, iptr, b, eps


def transpose_a(aelem, jptr, iptr):
    n = len(iptr)-1
    aelem1 = []
    jptr1 = []
    iptr1 = [0]
    current_row1 = 0
    counter1 = 0

    for row1 in range(n):
        for column1 in range(n):
            a = matrix(aelem,jptr, iptr,column1,row1)
            if row1 != current_row1:
                iptr1.append(counter1)
                current_row1 = row1
            if a != 0:
                aelem1.append(a)
                counter1 += 1
                jptr1.append(column1)

    iptr1.append(counter1)
    return aelem1, jptr1, iptr1


def matrix(aelem, jptr, iptr, i, j):
    """Интерфейс получения элемента по его индексам из сжатой матрицы"""
    res = 0
    n1 = iptr[i]
    n2 = iptr[i+1]
    for k in range(n1,n2):
        if jptr[k] == j:
            res = aelem[k]
            break
    return res


# def multiply_ata(aelem,jptr, iptr, aelemb, jptrb, iptrb):
#     m, n, l = len(iptr) - 1, len(iptr) - 1, len(iptrb) - 1
#     res = [[0.0 for _ in range(l)] for _ in range(m)]
#     for i in range(m):
#         for k in range(n):
#             if matrix(aelem, jptr, iptr, i, k):
#                 for j in range(l):
#                     res[i][j] += matrix(aelem, jptr,iptr,i,k)*matrix(aelemb, jptrb,iptrb,k,j)
#     print(csr(res))
#     return csr(res)


def multiply_ata(aelem,jptr, iptr, aelemb,jptrb, iptrb):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    m, n, l = len(iptr)-1, len(iptr)-1, len(iptrb)-1
    res = [[0 for _ in range(l)] for _ in range(m)]
    for i in range(m):
        for k in range(n):
            if matrix(aelem,jptr, iptr,i,k):
                for j in range(l):
                    res[i][j]+=matrix(aelem,jptr, iptr,i,k)*matrix(aelemb,jptrb, iptrb,k,j)
    #print(csr(res))
    return csr(res)


def csr(a):     #massiv strok
    aelem = []  #j  sto]bec, i stroka
    jptr = []
    iptr = [0]
    current_row = 0
    counter = 0
    for row in range(len(a)):
        for column in range(len(a[row])):
            if row != current_row:
                iptr.append(counter)
                current_row = row
            if a[row][column] != 0:
                aelem.append(a[row][column])
                counter += 1
                jptr.append(column)

    iptr.append(counter)

    return aelem, jptr, iptr


def multiply_atb(aelem, jptr, iptr, b):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    m, n, l = len(iptr)-1, len(iptr)-1, 1
    res = [[0.0 for _ in range(l)]for _ in range(m)]
    for i in range(m):
        for k in range(n):
            for j in range(l):
                res[i][j] += matrix(aelem, jptr, iptr, i, k) * b[k]
    #print([res[i][0] for i in range(m)])
    return [res[i][0] for i in range(m)]


def seidel(aelem, jptr, iptr, b, eps):
    """Разработать программу для численного решения СЛАУ методом Зейделя
    с организацией хранения сильно разреженной матрицы большой размерности"""

    n = len(iptr)-1
    x = [.0 for i in range(n)]
    converge = False

    aelemt, jptrt, iptrt = transpose_a(aelem,jptr, iptr)
    aelemata, jptrata, iptrata = multiply_ata(aelemt, jptrt, iptrt, aelem, jptr,iptr)
    bta = multiply_atb(aelemt, jptrt, iptrt, b)

    while not converge:
        x_new = deepcopy(x)
        for i in range(n):
            s1 = sum(matrix(aelemata, jptrata, iptrata,i, j) * x_new[j] for j in range(i))
            s2 = sum(matrix(aelemata, jptrata, iptrata,i, j) * x[j] for j in range(i + 1, n))
            x_new[i] = (bta[i] - s1 - s2) / matrix(aelemata, jptrata, iptrata,i, i)
        converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new

    return x


if __name__ == '__main__':
    # print(seidel([[3.6, 1.8, -4.7], [2.7, -3.6, 1.9], [1.5, 4.5, 3.3]], [3.8, 0.4, -1.6], 0.001))
    # print(seidel([[3.6, 2.7, 1.5], [1.8, -3.6, 4.5], [-4.7, 1.9, 3.3]], [3.8, 0.4, -1.6], 0.001))
    #print(seidel([3.6, 1.8, -4.7, 3.8, 2.7, -3.6, 1.9, 0.4, 1.5, 4.5, 3.3, -1.6], [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3], [0, 4, 8, 12], 0.001))
    #print(seidel([[0.945, -0.5882, 0, 0, 0], [-0.017, 0.9806, -0.0114, 0, 0], [0, -0.0153, 0.9876, -0.0107, 0], [0, 0, -0.1111, 0.9188, -0.5], [0, 0, 0, -0.75, 0.9378]], [50,-15.2371,-14.2308,0,-48], 0.0001))
    #[43.5987285945029, -14.959540119074564, -15.21082815402478, -52.57321995394093, -93.2287427654678]
    #print(seidel([0.945, -0.5882, 50.0, -0.017, 0.9806, -0.0114, -15.2371, -0.0153, 0.9876, -0.0107, -14.2308, -0.1111, 0.9188, -0.5, -0.75, 0.9378, -48.0], [0, 1, 5, 0, 1, 2, 5, 1, 2, 3, 5, 2, 3, 4, 3, 4, 5], [0, 3, 7, 11, 14, 17], 0.0001))
    #aelem, jptr, iptr,b, eps = input_into_scr()
    #print(seidel(aelem, jptr, iptr,b, eps))
    #print(seidel([3.6, 1.8, -4.7, 2.7, -3.6, 1.9, 1.5, 4.5, 3.3], [0, 1, 2, 0, 1, 2, 0, 1, 2], [0, 3, 6, 9], [3.8, 0.4, -1.6], 0.001))
    #print(seidel([5,7,1,9,10,13,2,0,11], [0,1,2,0,1,2,0,1,2],[0,3,6,9], [13,32,13],0.00000000000000000000000000000000000000000000000000000000001))
    print(seidel([5,7,1,10,14,2,2,0,11], [0,1,2,0,1,2,0,1,2],[0,3,6,9], [13,26,13],0.00000000000000000000000000000000000000000000000000000000001))