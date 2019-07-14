a,b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=[]
for i in c:
    if i<=i+1:
        d.append(i)
print(d[b-1])
