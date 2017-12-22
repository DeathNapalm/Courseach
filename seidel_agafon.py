#import random
n =3
# a = [[0.945,-0.5882,0,0,0],
#      [-0.017,0.9806,-0.0114,0,0],
#      [0,-0.0153,0.9876,-0.0107,0],
#      [0,0,-0.1111,0.9188,-0.5],
#      [0,0,0,-0.75,0.9378]]
#
# d = [50,-15.2371,-14.2308,0,-48]
a = [[5,7,1],[10,14,2],[2,0,11]]
d = [13,26,13]
x = [0]*n
b = [[0]*n]*n
g = [0]*n
x1 = [0]*n
xk = [0]*n
k = 0
print(a,d)

e = 0.1 #float(input('e?')) # probably eps

for j in range(n):
    g[j] = d[j];
    x[j] = g[j];
    x1[j] = x[j];
    for i in range(n):
        if i == j:
            b[j][i] = 1 - a[j][i]
        else:
            b[j][i] = -a[j][i]

print(b)

while True:
    y = 0
    k=k+1
    print('итерация ', k )
    for j in range(n):
        xk[j] = g[j]
        for i in range(n):
            xk[j] += b[j][i] * x1[i]
        x1[j] = xk[j]

    for j in range(n):
        z = abs(xk[j] - x[j])
        x[j] = xk[j]
        if z<e:
            y=y+1
    if y!=n:break


print(x)
input()


