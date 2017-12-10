from Python.Curseach.matrix import height


def gauss_seidel(m, x0=None, eps=1e-4, max_iteration=100):
    """
    Parameters
    ----------
    m  : list of list of floats : coefficient matrix
    x0 : list of floats : initial guess
    eps: float : error tolerance
    max_iteration: int

    Returns
    -------
    list of floats
        solution to the system of linear equation

    Raises
    ------
    ValueError
        Solution does not converge
    """
    n = height(m)
    x0 = [0] * n if x0 is None else x0
    x1 = x0[:]

    for __ in range(max_iteration):
        for i in range(n):
            s = sum(-m[i][j] * x1[j] for j in range(n) if i != j)
            x1[i] = (m[i][n] + s) / m[i][i]
        if all(abs(x1[i] - x0[i]) < eps for i in range(n)):
            return x1
        x0 = x1[:]
    raise ValueError('Solution does not converge')


if __name__ == '__main__':
    m = [[3.6, 1.8, -4.7, 3.8], [2.7, -3.6, 1.9, 0.4], [1.5, 4.5, 3.3,-1.6]]
    print(gauss_seidel(m))

    # author: Worasait Suwannik http://bit.ly/wannik
    # date: May 2015
