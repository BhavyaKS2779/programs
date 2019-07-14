s=input()
d=[]
for i in s:
    if i not in d:
        d.append(i)
print(*d[::-1],sep='')
