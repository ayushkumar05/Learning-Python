
def checkforprimenumber():
    n = 0
    x = int(input('input number to check wether it is prime or not'))
    if x>1:
        for a in range(2,x+1):
         

         if (x%a)==0:
             if x!= a:
                 print('factor',n,'is',a)
                 x = x/a
                 n+=1
 
             else:
                 print('number is prime')



    elif x==1:
        print('number is neither prime nor composite')
    elif x<0:
        print('number is composite')
    checkforprimenumber()

checkforprimenumber()

