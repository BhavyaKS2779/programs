n=int(input())
a=list(map(int,input().split()))
l=[]
if(sorted(set(a))==sorted(a)):
    print("unique")
else:
    for i in a:
        if a.count(i)>1:
            l.append(i)
    print(*set(sorted(l)))
    

    
    

    
    

