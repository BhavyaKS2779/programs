a=int(input())
temp=a
c=0
while a!=1:
    a=a//2
    c=c+1
d=2**c
if (temp==d):
    print("yes")
else:
    print("no")
    
