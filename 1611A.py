t = int(input())
for _ in range(t):
    n = input()
    if int(n)%2==0:
        print(0)
    elif any(True for i in n if int(i)%2==0):
        if int(n[0])%2==0:
            print(1)
        else:
            print(2)
    else:
        print(-1)
    
