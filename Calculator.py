import math

TITLE='Calculator'

def menu():
    print('')
    print('Operations:')
    print('Addition: +')
    print('Subtraction: -')
    print('Multiplication: *')
    print('Exponent: **')
    print('Division: /')
    print('Floor Division: //')
    print('Modulus: %')
    print('Sin(a): sin')
    print('Cos(a): cos')
    print('Log(a): log')
    print('Sqrt(a): sqrt')
    print('Exit: q')
    return input('Enter operator (+|-|*|**|/|//|%|sin|cos|log|sqrt): ')
    
running = True
while running:

    # Store the user input an operator
    o = menu()

    # Exit
    if o == 'q':
        print('Thank you for using ' + TITLE + '!')
        break

    # Enter a and b
    a = int(input("Enter a: "))
    if o not in ('sin', 'cos', 'log', 'sqrt'):
        b = int(input("Enter b: "))   
       

    # Run calculation
    if o == "+":
        print("a + b = ", a + b)
    elif o == '-':
        print("a - b = ", a - b)
    elif o == '*':
        print("a * b = ", a * b)
    elif o == '/':
        if b != 0:
            print("a / b = ", a / b)
        else:
            print("Oops, division by zero")
    elif o == '//':
        if b != 0:
            print ("a // b = ", a // b)
        else:
            print("Oops, division by zero")
    elif o == '**':
        print("a ^ b = ", a ** b)
    elif o == '%':
        if a !=0:
            print("a % b = ", a % b)
        else:
            print("Oops, division by zero")
    elif o == 'sin':
        print ("sin(a) = ", math.sin(math.radians(a)))
    elif o == 'cos':
        print ("cos(a) = ", math.cos(math.radians(a)))
    elif o == 'log':
        print ("log(a) = ", math.log(a))
    elif o == 'sqrt':
        print ("sqrt(a) = ", math.sqrt(a))
        
    # If none of the above conditions were true then execute this by default
    else:
        print("Use either + - * / %, cos, sin, log, sqrt next time")
