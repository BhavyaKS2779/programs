am=list(input())
dad=len(am)
for i in range(0,dad,2):
    am[i],am[i+1]=am[i+1],am[i]
print(*am,sep="")
