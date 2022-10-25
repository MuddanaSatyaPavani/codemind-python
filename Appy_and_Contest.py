t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    l=0
    if a%b==0:
        l=a
    elif b%a==0:
        l=b
    else:
        l=a*b
    x=n//l
    y=n//a
    z=n//b
    y=y-x
    z=z-x
    if y+z>=k:
        print("Win")
    else:
        print("Lose")