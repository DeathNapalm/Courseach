from math import sqrt

n = 3
eps = 0.0001
a = [[5,7,1],[9,10,13],[2,0,11]]

b = [13,32,13]
x = [0]*n
p = [0]*n


def converge(xk,xkp):
    norm = 0.0
    for i in range(n):
        norm += (xk[i] - xkp[i]) * (xk[i] - xkp[i])
    if sqrt(norm)>=eps:
        return False
    return True


while True:
    for i in range(n):
        p[i] = x[i]
    for i in range(n):
        var = 0.0
        for j in range(n):
            var += (a[i][j] * x[j])
        for j in range(n):
            var += (a[i][j] * p[j])
        x[i] = (b[i] - var) // a[i][i]
    if not converge(x,p): break


print(x)