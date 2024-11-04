t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    t=a.copy()
    m1=max(a)
    a.remove(m1)
    m2=max(a)

    for i in t:
        if i==m1:
            print(i-m2,end=" ")
        else:
            print(i-m1,end=" ")
    print()


