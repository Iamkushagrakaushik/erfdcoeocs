t = int(input())
for _ in range(t):
    n = int(input())
    s=input()
    m=""
     
    empty=True
    for i in s:
        if empty==True:
            c=i
            m+=i
            empty=False
            continue

        if i==c:
            empty=True
    print(m)

