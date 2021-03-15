def fn():
    x = int(input('check factors'))
    print('the factors of the number',x,' are')
    if x>1:
        while x>=1:
            for a in range(2,x):

             if (x%a)==0:

                 
                 print(a)
                 x = (x/a)
                 x=int(x)
                 break
             
                 
             else:
                 print(x)
                 print('1')
                 x=1
                 break





    elif x==1:
        print('number is neither prime nor composite')
    elif x<0:
        print('number is composite')

fn()
    
