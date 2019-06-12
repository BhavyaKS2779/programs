n,k=map(int,input().split())
d=input().split()
c=0
l=[]
for i in d:
    l.append(int(i))
for j in range(0,len(d)):
    if l[j]==k:
        c+=1
print(c)
