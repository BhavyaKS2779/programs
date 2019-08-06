n=input()
c=0
for i in n:
    f=n.count(i)
    if f>c:
       c=f
       letter=i
print(letter)
