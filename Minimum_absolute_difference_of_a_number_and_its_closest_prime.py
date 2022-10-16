
num=int(input())
a=num-1
while True:
    prime=True
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            prime=False
            break
    if prime==True:
        break
    else:
        a-=1
#print(a)
b=num
while True:
    prime=True
    for i in range(2,int(b**0.5)+1):
        if b%i==0:
            prime=False
            break
    if prime==True:
        break
    else:
        b+=1
#print(b)
d1=b-num
d2=num-a
if d1>d2:
    print(d2)
else:
    print(d1)
	