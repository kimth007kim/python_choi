a= 2
b= 10
for i in range(a,b+1):
    for j in range(a,b+1):
        if i%j==0:
            break
    if i==j:
        print(j,end=" ")