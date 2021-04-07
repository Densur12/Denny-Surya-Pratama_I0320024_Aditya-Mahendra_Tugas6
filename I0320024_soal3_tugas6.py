for i in range(10,25) :
    for j in range(2, i):
        if (i % j) == 0:
            print(i, 'bukan prima')
            break
    else:
        print(i, 'adalah bilangan prima')