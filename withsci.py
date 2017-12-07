import numpy as np
from scipy.sparse import csr_matrix
import scipy

#print(csr_matrix((3, 4), dtype=np.int8).toarray())
# array([[0, 0, 0, 0],
#        [0, 0, 0, 0],
#        [0, 0, 0, 0]], dtype=int8)


a = np.array([[9,0,0,3,1,0,1],
               [0,11,2,1,0,0,2],
               [0,1,10,2,0,0,0],
               [2,1,2,9,1,0,0],
               [1,0,0,1,12,0,1],
               [0,0,0,0,0,8,0],
               [2,2,0,0,3,0,8]])

b =csr_matrix(a)
print (b.data, b.indices, b.indptr, sep='\n')

#([9, 3, 1, 1, 11, 2, 1, 2, 1, 10, 2, 2, 1, 2, 9, 1, 1, 1, 12, 1, 8, 2, 2, 3, 8],
#  [0, 3, 4, 6, 1, 2, 3, 6, 1, 2, 3, 0, 1, 2, 3, 4, 0, 3, 4, 6, 5, 0, 1, 4, 6],
#  [0, 5, 9, 12, 17, 21, 22, 25])

if __name__ == '__main__':
    pass