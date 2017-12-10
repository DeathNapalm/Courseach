def scr(a):     #massiv strok
    aelem = []  #j  sto]bec, i stroka
    jptr = []
    iptr = [0]
    current_row = 0
    counter = 0
    for row in range(len(a)):
        for column in range(len(a[row])):
            if a[row][column] != 0:
                aelem.append(a[row][column])
                counter += 1
                jptr.append(column)
                if row != current_row:
                    iptr.append(counter-1)
                    current_row = row
    iptr.append(counter)


    return aelem, jptr, iptr


if __name__ == '__main__':
    # print(scr([[9,0,0,3,1,0,1],
    #            [0,11,2,1,0,0,2],
    #            [0,1,10,2,0,0,0],
    #            [2,1,2,9,1,0,0],
    #            [1,0,0,1,12,0,1],
    #            [0,0,0,0,0,8,0],
    #            [2,2,0,0,3,0,8]]))

    print(scr([[0.17, 0.75, -0.18, 0.21, 0.11],
                       [0.75, 0.13, 0.11, 1.0, 2.0],
                       [-0.33, 0.11, 3.01, -2.01, 0.11],
                       [0.11, 1.12, 1.11, -1.31, 0.13]]))

    # print(scr([[0, 2, 0, 1, 0, 0],
    #            [0, 0, 0, 0, 0, 0],
    #            [0, 5, 0, 0, 0, 1],
    #            [0, 0, 0, 0, 9, 1],
    #            [0, 0, 0, 0, 0, 0],
    #            [0, 8, 0, 4, 0, 3]]))


