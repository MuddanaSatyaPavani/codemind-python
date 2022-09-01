l,r,k=map(int,input().split())
sum=0
for i in range(l,r+1):
    if i%k==0:
        sum=sum+1
print(sum)