s = 0
a = 2
ans = []
y = 0
answer = 0
x = int(input('enter limit'))
for i in range(1,x+1):
    s = s+ (a**2)
    ans.append(s)
    a +=2
    
print(ans)
for j in range (0,x):
    answer = answer + ans[j]

print(answer)
