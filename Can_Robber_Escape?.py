n=int(input())
l=map(int,input().split())
for i in l:
    if i>=n:
        print("NO")
        break
else:
    print("YES")