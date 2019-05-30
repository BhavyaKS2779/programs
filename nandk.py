import sys
n,k=map(int,sys.stdin.readline().split(' '))
l=list(map(int,input().split()))
a=0
for i in range(k):
  a=a+l[i]
print(a)
