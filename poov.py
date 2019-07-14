a,b=map(int,input().split())
c=input().split()
d=[]
for i in c:
    if (int(i)%2!=0):
        d.append(i)
print(d[b-1])
    
