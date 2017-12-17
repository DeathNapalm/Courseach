#from Python.Curseach import matrix


def input_into_scr(l):     #massiv strok
    """Ввод матрицы с клавиатуры с параллельным переводом в сжатый формат"""
    eps = float(input('Введите точность: '))
    n = int(input('введите количество строк: '))
    aelem = []  #j  sto]bec, i stroka
    jptr = []
    iptr = [0]
    current_row = 0
    counter = 0
    for row in range(n):
        for column in range(n+1):
            a = float(input('введите а[{}][{}]: '.format(row,column)))
            if row != current_row:
                iptr.append(counter)
                current_row = row
            if a != 0:
                aelem.append(a)
                counter += 1
                jptr.append(column)

    iptr.append(counter)
    return aelem, jptr, iptr, eps



def matrix(alem,jptr,iptr,i,j):
    """int procedure(i,j)
        {
            AA=0; // значение искомого элемента
            N1=LI[i];
            N2=LI[i+1];
            for(k=N1;k<N2;k++)
            {
                if (LJ[k]==j)
                {
                    AA=A[k];
                    <break>;
                }
            }
            return AA;
        }"""

    res = 0
    n1 = iptr[i]
    n2 = iptr[i+1]
    for k in range(n1,n2):
        if jptr[k] == j:
            res = alem[k]
            break
    return res
#x =[3.6, 1.8, -4.7, 3.8, 2.7, -3.6, 1.9, 0.4, 1.5, 4.5, 3.3, -1.6]
#y = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]


#print(list(reversed(x)))

#print([3-n for n in y])



#[-1.6, 3.3, 4.5, 1.5, 0.4, 1.9, -3.6, 2.7, 3.8, -4.7, 1.8, 3.6], [3, 2, 1, 0, 3, 2, 1, 0, 3, 2, 1, 0], [0, 4, 8, 12]
#aelem, jptr, iptr = [3.6, 1.8, -4.7, 2.7, -3.6, 1.9, 1.5, 4.5, 3.3], [0, 1, 2, 0, 1, 2, 0, 1, 2], [0, 3, 6, 9]

#n = 3

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

if __name__ == '__main__':
    print(transpose_a([3.6, 1.8, -4.7, 2.7, -3.6, 1.9, 1.5, 4.5, 3.3], [0, 1, 2, 0, 1, 2, 0, 1, 2], [0, 3, 6, 9]))



#z[ 3.6  2.7  1.5  1.8 -3.6  4.5 -4.7  1.9  3.3],[0 1 2 0 1 2 0 1 2],[0 3 6 9]


