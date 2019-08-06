a,b=map(int,input().split())
c=list(map(int,input().split()))
print(*(c[b:]+c[:b]))
