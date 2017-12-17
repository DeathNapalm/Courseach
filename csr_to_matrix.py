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
    check = [[0]*3]*3
    for i in range(3):
        for j in range(3):
            print(matrix([ 3.6 , 2.7,  1.5 , 1.8, -3.6 , 4.5 ,-4.7 , 1.9 , 3.3],[0 ,1, 2 ,0 ,1, 2 ,0 ,1 ,2],[0 ,3, 6 ,9],i,j),sep='\t',  end=' ')
        print('\n')
    #for row in check:
    #print(check)
    #sep='\t',