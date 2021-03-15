x = int(input('enter a number'))
sum1=0
sum2=0

while x>0:
    if x%2==0:
        sum1+=x
        x-=1
    else:
        sum2+=x
        x-=1

print('sum of even numbers ->',sum1)
print('sum of odd numbers is ->',sum2)
        
