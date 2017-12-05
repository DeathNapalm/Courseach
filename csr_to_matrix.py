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
    for i in range(n1,n2):
        if jptr[i] == j:
            res =alem[i]
            break
    return res