n=int(input())
x=list(map(int,input().split()))
even=0
odd=0
for i in range(len(x)):
    if i%2==0:
        even+=x[i]
    else:
        odd+=x[i]
a=abs(even-odd)
print(a)