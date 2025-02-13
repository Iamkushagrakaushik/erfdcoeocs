t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c=0
    avg=sum(a)
    if avg%n!=0:
        print(-1)
        continue
    avg//=n
    for i in a:
        if i>avg:
            c+=1
    print(c)

