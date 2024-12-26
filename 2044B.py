t=int(input())
for _ in range(t):
    s1=input()
    s=s1[::-1]
    m=""
    for i in s:
        if i=='p':
            m+='q'
        elif i=='q':
            m+='p'
        else:
            m+='w'
    print(m)
