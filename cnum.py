n=str(input())
c=0
for i in range(len(n)):
    if n[i].isnumeric():
        c+=1
print(c)
