t = int(input())
for _ in range(t):
    n = int(input())
    d={}
    for i in range(n):
        s=input()
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
    for i in d:
        if d[i]%n!=0:
            print("NO")
            break
    else:
        print("YES")

