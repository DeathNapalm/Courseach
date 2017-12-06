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
        for j in range(7):
            check[i][j] = matrix([9, 3, 1, 1, 11, 2, 1, 2, 1, 10, 2, 2, 1, 2, 9, 1, 1, 1, 12, 1, 8, 2, 2, 3, 8],
                                 [1, 4, 5, 7, 2, 3, 4, 7, 2, 3, 4, 1, 2, 3, 4, 5, 1, 4, 5, 7, 6, 1, 2, 5, 7],
                                 [1, 5, 9, 12, 17, 21, 22, 26], i, j)
    for row in check:
        print(row)