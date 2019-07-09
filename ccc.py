n,b=list(map(int,input().split()))
c=0
for i in range(n,b+1):
    if i>1:
        for e in range(2,i):
            if(i%e==0):
                break
        else:
            c+=1
print(c)
