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




def multiply_ata(aelem,jptr, iptr, b):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    m, n, l = len(iptr)-1, len(iptr)-1, 1
    res = [[0 for _ in range(l)] for _ in range(m)]
    for i in range(m):
        for k in range(n):
            for j in range(l):
                res[i][j] += matrix(aelem, jptr, iptr, i, k) * b[k]
    return res



if __name__ == '__main__':
    print(multiply_ata([3.6, 2.7, 1.5, 1.8, -3.6, 4.5,-4.7, 1.9, 3.3],[0, 1, 2, 0, 1, 2, 0, 1, 2], [0, 3, 6, 9],  [3.8, 0.4, -1.6]))

    # [22.5, 3.51, -6.840000000000003],
    # [3.51, 36.45, -0.45000000000000107],
    # [-6.840000000000003, -0.45000000000000107, 36.59]