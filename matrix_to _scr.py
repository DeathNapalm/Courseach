def scr(a):     #massiv strok
    aelem = []  #j  sto]bec, i stroka
    jptr = []
    iptr = []
    for row in range(len(a)):
        current_row = 0
        for column in range(len(row)):
            if a[row][column] != 0:
                aelem.append(a[row][column])
                jptr.append(column)
                if row != current_row:
                    iptr.append(row)
if __name__ == '__main__':
    print(csr[[9,0,0,3,1,0,1],
              [0,11,2,1,0,0,2],
              [0,0,1,0,0,0,0],
              [2,1,2,9,1,0,0],
              [1,0,0,1,12,0,1],
              [0,0,0,0,0,8,0],
              [2,2,0,0,3,0,8]])


