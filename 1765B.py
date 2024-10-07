t=int(input())
a=[]
for _ in range(t):
    n=int(input())
    s=input()
    if n%3==2:
        a.append("NO")
    else:
        for i in range(0,n-n%3,3):
            c=s[i:i+3]
            if c[1]!=c[2]:
                a.append("NO")
                break
        else:
            a.append("YES")
for i in a :
    print(i)
