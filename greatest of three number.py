def greatestnum():

    a = float(input('enter number'))
    a1 = float(input('enter number'))
    a2 = float(input('enter number'))

    if a>a1 and a>a2:
        print('the greatest number is',+a)

    elif a1>a and a1>a2:
        print('the greatest number is',+a1)

    elif a2>a1 and a2>a:
        print('the greatest number is',+a2)

    elif a<a1 and a>a2:
        print('the greatest number is',+a)

    elif a1>a and a1>a2:
        print('the greatest number is',+a1)

    elif a2>a1 and a2>a:
        print('the greatest number is',+a2)

    elif a==a1 and a1==a2:
        print('all are equal')

    greatestnum()

greatestnum()

    
