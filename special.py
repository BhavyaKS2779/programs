number=input()
count=0
for i in number:
    if(i.isalpha()==True):
        continue
    elif(i.isdigit()==True):
        continue
    elif(i==" "):
        continue
    else:
        count=count+1
print(count)
