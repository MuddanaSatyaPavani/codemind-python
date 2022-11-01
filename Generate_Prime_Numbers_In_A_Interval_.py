n=int(input())
m=int(input())
def prime(u):
    f=0
    for i in range(1,u+1):
        if u%i==0:
            f=f+1
    if f==2:
        return True
for i in range(n,m+1):
    if prime(i)==True:
        print(i)