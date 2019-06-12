n=input()
c=0
for i in n:
    if ((i=='0') or (i=='1')):
        c+=1
if(c==len(n)):
    print("yes")
else:
    print("no")
