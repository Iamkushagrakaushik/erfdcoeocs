t = int(input())
for _ in range(t):
    n = int(input())
    s=input()
    d={}
    m=0
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d.keys():
        c=ord(i)-64
        if d[i]>=c:
            m+=1
    print(m)

