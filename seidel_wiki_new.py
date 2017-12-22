import math

#n = 5
n = 3
eps = 0.1
# a = [[0.945, -0.5882, 0, 0, 0],
#      [-0.017, 0.9806, -0.0114, 0, 0],
#      [0, -0.0153, 0.9876, -0.0107, 0],
#      [0, 0, -0.1111, 0.9188, -0.5],
#      [0, 0, 0, -0.75, 0.9378]]

# b = [50,-15.2371,-14.2308,0,-48]
a = [[5,7,1],[10,14,2],[2,0,11]]
b = [13,26,13]
x = [0]*n
p = [0]*n


def converge(xk,xkp):
    norm = 0.0
    for i in range(n):
        norm += (xk[i] - xkp[i]) * (xk[i] - xkp[i])
    if math.sqrt(norm)>=eps:
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