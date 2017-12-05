def scr(a):     #massiv strok
    aelem = []  #j  sto]bec, i stroka
    jptr = []
    iptr = []
    for row in range(len(a)):
        for column in range(len(row)):
            if a[row][column] != 0:
                aelem.append(a[row][column])
                jptr.append(column)

