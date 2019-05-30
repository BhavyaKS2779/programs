n=int(input("enter the number"))
sum=0
temp=n
order=len(str(n))
while(n>0):
  digit=n%10
  sum+=digit**order
if(temp==n):
  print(" Yes")
else:
  print("No")
  
