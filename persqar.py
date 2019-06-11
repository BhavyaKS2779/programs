import math
n,m=map(int,input().split())
b=n*m
root=math.sqrt(b)
if root*root==b:
    print("yes")
else:
    print("no")
