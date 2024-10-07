t=int(input())
for _ in range(t):
    s=""
    for _ in range(8):
        a=input()
        s+=a
    c=""
    for i in s:
        if i=='.':
            pass
        else:
            c+=i
    print(c)