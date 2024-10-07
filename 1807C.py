t=int(input())
for _ in range(t):
    d={}
    c=1
    n=int(input())
    s=input()
    for i in range(n):
        if s[i] in d:
            pass
        else:
            d[s[i]]=i
    for i in d.keys():
        for j in range(d[i]+1,n,2):
            if s[j]==i:
                c=0
                print("NO")
                break
        if c==0:
            break
    else:
        print("YES")
        
