n=int(input())
x=list(map(int,input().split()))
even=0
for i in range(len(x)):
    if x[i]%2==0:
        even+=x[i]
print(even)