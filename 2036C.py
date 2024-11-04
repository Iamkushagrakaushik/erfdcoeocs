t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    q=int(input())
    for _ in range(q):
        a,b=map(int,input().split())
        if n<4:
            print("NO")
        else:
            s=s[0:a-1]+str(b)+s[a:]
            if "1100" in s:
                print("YES")
            else:
                print("NO")             
