n=int(input("enter the number of lines"))
l =0
k =0
for i in range (1,n+1):
    for s in range (i-n,1,1):
        print(" ", end=" ")
    for j in range (1,i+1):
        print(j ,end=" ")

    j = j-1

    for k in range(j,0,-1):
        print(k,end =' ')
            
    print()
