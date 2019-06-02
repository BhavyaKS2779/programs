a,b=map(int,input().split())
for i in range(a,b):
    temp=i
    sum=0
    a=len(str(i))
    while temp>0:
        digit=temp%10
        sum=sum+digit**a
        temp=temp//10
    if i==sum:
        print(i)
