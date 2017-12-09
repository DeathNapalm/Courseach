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


if __name__ == '__main__':
    check = [[0]*6]*6
    for i in range(6):
        print('\n')
        for j in range(6):
            print(matrix([2 ,5 ,9 ,1, 3, 8, 4], [2, 1, 4, 5, 5, 0, 3], [0, 1, 1, 2 ,4 ,5, 7], i, j), end=' ')

    #for row in check:
    #print(check)