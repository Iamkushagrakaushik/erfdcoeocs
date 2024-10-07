t=int(input())
a=[]
for _ in range(t):
    s=input()
    n=len(s)
    if n==2:
        a.append(s)
    else:
        i=0
        x=""
        while i<n:
            x+=s[i]
            i+=2
        x+=s[-1]
        a.append(x)
for i in a:
    print(i)