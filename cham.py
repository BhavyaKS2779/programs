n=int(input())
c=0
while n>0:
    dig=n%10
    c+=dig*dig
    n=n//10
print(c)
