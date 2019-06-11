a=int(input())
b,c=list(map(int,input().split()))
for i in range(b,c):
    print("yes")
    break
else:
    print("no")
