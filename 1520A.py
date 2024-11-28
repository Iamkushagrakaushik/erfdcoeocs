t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    
    for i in range(n):
        t=s[i]
        c=0
        f=1

        for j in range(i+1,n):
            if s[j]!=t:
                if c==0:
                    c=1
            else:
                if c==1:
                    print("NO")
                    f=0
                    break
        if f==0:
            break
    else:
        print("YES")




