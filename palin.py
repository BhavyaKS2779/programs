n=int(input())
sum=0
rev=0
while n>0:
    rem=n%10
    sum+=rem
    n=n//10
temp=sum
while sum>0:
    rem1=sum%10
    rev=rev*10+rem1
    sum=sum//10
if(rev==temp):
    print("YES")
else:
    print("NO")
