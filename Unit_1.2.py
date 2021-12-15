def calculateTringleSquare():
    running=True
    while running:
        a=input('Enter triangle side 1: ')
        if a.isnumeric():
            a=int(a)
            running=False
        else:
            print('Please enter number!')

    running=True
    while running:
        b=input('Enter triangle side 2: ')
        if b.isnumeric():
            b=int(b)
            running=False
        else:
            print('Please enter number!')

    s = ((1/2)*a*b)

    print('Square of a triangle is: ', s)

calculateTringleSquare()
    
