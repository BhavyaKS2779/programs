a=input()
b=""
c=""
for i in range(0,len(a)):
    if i%2==0:
        b=b+a[i]
    else:
        c=c+a[i]
print(b,c)
