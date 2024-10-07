t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    x=0
    a,b,c,d=0,0,0,0
    for i in s:
        if i=='A':
            a+=1
        elif i=='B':
            b+=1
        elif i=='C':
            c+=1
        elif i=='D':
            d+=1
    
    x=min(a,n)+min(b,n)+min(c,n)+min(d,n)
    print(x)