n=input()
b=list(map(int,input().split()))
c=0
d=len(b)
for i in range(len(b)):
    c=c+int(b[i])
    e=c//d
print(e)
