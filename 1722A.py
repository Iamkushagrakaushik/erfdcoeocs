t=int(input())
x="Timru"
a=[]
for _ in range(t):
    n=int(input())
    s=input()
    if n==5:
        m=''.join(sorted(s))
        if m==x:
            a.append("YES")
        else:
            a.append("NO")
    else:
        a.append("NO")
        
for i in a:
    print(i)