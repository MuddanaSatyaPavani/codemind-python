n=int(input())
s=0
a=list(map(int,input().split()))
for i in range(len(a)):
    s+=a[i]
x=s/n
print("{:.2f}".format(x))