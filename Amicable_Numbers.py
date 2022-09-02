n=int(input())
m=int(input())
s=0
t=0
for i in range(1,n):
    if n%i==0:
        s=s+i
for i in range(1,m):
    if m%i==0:
        t=t+i
if n==t or m==s:
    print("Amicable")
else:
    print("Not Amicable")