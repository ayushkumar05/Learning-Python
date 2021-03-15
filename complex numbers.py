import cmath

def complexnum():

    x = int(input('enter real part'))
    y = int(input('enter coeff of iota'))
    z = input('enter 1 for addition and 2 for subtraction')
    
    lo =  y*cmath.sqrt(-1)

    if z == '1':
        a = x+ lo
    elif z =='2':
        a = x - lo
    else:
        print('not gonna work nigga')
        a =1
        
    if a == 1:
        print('what did i tell ya!?!?!?!?')

    else:
        
        print('the complex number is:')
        print(a)
        input()

        print( 'square root of the complex number is :')
        print(cmath.sqrt(a))

    print('polar form is:')
    print(cmath.polar(a))
    print('argument is :')
    print(cmath.phase(a))

    complexnum()
    
complexnum()

