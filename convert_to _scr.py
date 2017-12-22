def scr(a):     #massiv strok
    aelem = []  #j  sto]bec, i stroka
    jptr = []
    iptr = [0]
    current_row = 0
    counter = 0
    for row in range(len(a)):
        for column in range(len(a[row])):
            if row != current_row:
                iptr.append(counter)
                current_row = row
            if a[row][column] != 0:
                aelem.append(a[row][column])
                counter += 1
                jptr.append(column)

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

    #print(scr([[3.6, 1.8, -4.7, 3.8], [2.7, -3.6, 1.9, 0.4], [1.5, 4.5, 3.3,-1.6]]))
    print(scr([[3.6, 1.8, -4.7], [2.7, -3.6, 1.9], [1.5, 4.5, 3.3]]))
    #print(scr([[22.5, 3.51, -6.840000000000003],[3.51, 36.45, -0.45000000000000107],[-6.840000000000003, -0.45000000000000107, 36.59]]))

    # print(scr([[0, 2, 0, 1, 0, 0],
    #            [0, 0, 0, 0, 0, 0],
    #            [0, 5, 0, 0, 0, 1],
    #            [0, 0, 0, 0, 9, 1],
    #            [0, 0, 0, 0, 0, 0],
    #            [0, 8, 0, 4, 0, 3]]))


#[ 0  3  7 11 14 17]