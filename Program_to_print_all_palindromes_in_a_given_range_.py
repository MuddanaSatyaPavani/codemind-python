a=int(input())
b=int(input())

for i in range(a,b+1):
   n1=i
   n2=0
   while(n1!=0):
      rem=n1%10
      n1=int(n1/10)
      n2=n2*10+rem
   if(i==n2):
      print(i,end=" ")