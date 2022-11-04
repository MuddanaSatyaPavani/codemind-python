a=int(input())
b=list(map(int,input().split()))
s=0
for i in b:
    s=s+i
x=s//a
if x in b:
    print("True")
else:
    print("False")