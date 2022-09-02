import math
x,y,M=map(int,input().split())
s=math.pow(x,y)
a=s%M
print(int(a))