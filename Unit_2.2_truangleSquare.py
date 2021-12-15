from math import sin, radians
def triangleSquare():
    side=int(input('Enter triangle side: '))
    corner1=int(input('Enter triangle corner 1: '))
    corner2=int(input('Enter triangle corner 2: '))

    if corner1+corner2<180:
        print('Triangle square is:', (side**2)/2*(sin(radians(corner1))*sin(radians(corner2)))/sin(radians(180-corner1-corner2)))
    else:
        print('Can\'t calculate triangle square. Sum of 2 corners is equal or more 180 digrees')

triangleSquare()


                                                    
    
