import numpy as np
from scipy.sparse import csr_matrix
import scipy


def withsci(a):
    a = np.array(a)
    b =csr_matrix(a)
    return b.data, b.indices, b.indptr


if __name__ == '__main__':
    print(withsci([[0.17, 0.75, -0.18, 0.21, 0.11],
                          [0.75, 0.13, 0.11, 1, 2],
                          [-0.33, 0.11, 3.01, -2.01, 0.11],
                          [0.11, 1.12, 1.11, -1.31, 0,13]]))