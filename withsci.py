import numpy as np
from scipy.sparse import csr_matrix
import scipy


def withsci(a):
    a = np.array(a)
    b = csr_matrix(a)
    return b.data, b.indices, b.indptr


if __name__ == '__main__':
    #withsci(1)
    # arrays = np.array([[0.945,-0.5882,0,0,0,50],
    #                     [-0.017,0.9806,-0.0114,0,0,-15.2371],
    #                     [0,-0.0153,0.9876,-0.0107,0,-14.2308],
    #                     [0,0,-0.1111,0.9188,-0.5,0],
    #                     [0,0,0,-0.75,0.9378,-48]])
    arrays = np.array([[3.6, 1.8, -4.7], [2.7, -3.6, 1.9], [1.5, 4.5, 3.3]])
    arrays  = arrays.transpose()
    brrays = csr_matrix(arrays)
    #brrays = brrays .transpose()
    print(brrays.data, brrays.indices, brrays.indptr, sep=',')


    #[50,-15.2371,-14.2308,0,-48]