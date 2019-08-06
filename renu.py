n=int(input())
a=list(map(int,input().split()))
l=[]
for i in a:
    if a.count(i)==1:
        l.append(i)
print(*l)
