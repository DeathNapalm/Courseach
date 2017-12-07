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
    check = [[0]*7]*7
    #print(check,sep='\n')
    for i in range(7):
        print('\n')
        for j in range(7):
            print(matrix([9, 3, 1, 1, 11, 2, 1, 2, 1, 10, 2, 2, 1, 2, 9, 1, 1, 1, 12, 1, 8, 2, 2, 3, 8],
                                 [0, 3, 4, 6, 1, 2, 3, 6, 1, 2, 3, 0, 1, 2, 3, 4, 0, 3, 4, 6, 5, 0, 1, 4, 6],
                                 [0, 4, 8, 11, 16, 20, 21, 25], i, j), end=' ')

    #for row in check:
    #print(check)