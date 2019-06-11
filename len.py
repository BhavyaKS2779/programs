n=list(input())
b=len(n)-1
if b%2!=0:
    n[b//2]="*"
    n[b//2+1]="*"
else:
    n[b//2]="*"
print("".join(n))
