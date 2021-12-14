def checkNumbers():
    a= input ('Enter integer value: ')

    if a.isnumeric():
        a=int(a)
        print('The next number for the number ', a, ' is ', a+1)
        print('The previous number for the number ', a, ' is ', a-1)

checkNumbers()
