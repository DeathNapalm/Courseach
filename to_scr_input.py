def input_into_scr():     #massiv strok
    n = int(input('введите количество строк: '))
    aelem = []  #j  sto]bec, i stroka
    jptr = []
    iptr = [0]
    current_row = 0
    counter = 0
    for row in range(n):
        for column in range(n+1):
            a = float(input('введите а[{}][{}]: '.format(row,column)))
            if a != 0:
                aelem.append(a)
                counter += 1
                jptr.append(column)
            if row != current_row:
                iptr.append(counter-1)
                current_row = row
    iptr.append(counter)


    return aelem, jptr, iptr


if __name__ == '__main__':
    print(input_into_scr())