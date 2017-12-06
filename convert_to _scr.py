def scr(a):     #massiv strok
    aelem = []  #j  sto]bec, i stroka
    jptr = []
    iptr = []
    current_row = 0
    counter = 0
    for row in range(len(a)):
        for column in range(len(a[row])):
            if a[row][column] != 0:
                aelem.append(a[row][column])
                counter += 1
                jptr.append(column+1)
                if row != current_row:
                    iptr.append(counter)
                    current_row = row
    iptr.append(counter+1)


    return aelem, jptr, iptr


if __name__ == '__main__':
    print(scr([[9,0,0,3,1,0,1],
               [0,11,2,1,0,0,2],
               [0,1,10,2,0,0,0],
               [2,1,2,9,1,0,0],
               [1,0,0,1,12,0,1],
               [0,0,0,0,0,8,0],
               [2,2,0,0,3,0,8]]))


