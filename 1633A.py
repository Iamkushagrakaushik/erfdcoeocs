t=int(input())
for _ in range(t):
    n=int(input())
    if n%7==0:
        print(n)
        continue
     
    s=n//10
    s*=10
    for i in range(10):
        if (s+i)%7==0:

            print(s+i)
            break
    
