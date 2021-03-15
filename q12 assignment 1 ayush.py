def q12():

 name = input('what is thy name ')

 print('hi, '+name+' I shall serve you today')
 a = input('enter num 1')
 b =  input('enter number 2')

 x = int(a)

 y = int(b)

 choice = input('enter 1 for addidtion, 2 for multiplication, 3 for subtraction,4 for division, 5 for raised to the power, 6 for modulus,7 for comparing them')  

 if choice == '1':
  print('these numbers will be added')
  print(x+y)

 elif choice == '2': 
  print('these numbers will be multiplied')
  print(x*y)
 elif choice == '3':  
  print('these numbers will be subtracted')
  print(x-y)
 elif choice == '4':  
  print('these numbers will be divided')
  print(x/y)
 elif choice == '5':  
  print('x raised to the power y')
  print(x**y)
 elif choice == '6':
  print('remainder is')
  print(x%y)
 elif choice == '7':

     print('is x>y')

     print(x>y)
     print('is x<y')

     print(x<y)
     print('is x=y')

     print(x==y)

     print('is x>=y')

     print(x>=y)

     print('is x<y')

     print(x<=y)
     print('is x not equal to y')

     print(x!=y)


q12()
