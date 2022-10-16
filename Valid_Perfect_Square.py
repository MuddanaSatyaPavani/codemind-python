t=int(input())
for i in range(t):
    n=int(input())
    for i in range(n + 1): 
        pow = i * i
        if pow == n:
            print("True")
            break
        elif pow > n:
            print("False")
            break