n=input()
a=0
b=0
for i in n:
    if i.isalpha()==True:
        a=1
    elif i.isdigit()==True:
        b=1
if (a==1 and b==1):
    print("Yes")
else:
    print("No")
