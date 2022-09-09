n=int(input())
i=1
op=0
while i<=n:
    op+=1/i
    i+=1
print("{:.2f}".format(op))