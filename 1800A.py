t=int(input())
for _ in range(t):
    n=int(input())
    s=input().lower()
    if s[0]=='m' :
        s1=list(set(s))
        s1.sort()
        if s1==['e','m','o','w']:
            print("YES")
        else:
            print("NO")

    else:
        print("NO")