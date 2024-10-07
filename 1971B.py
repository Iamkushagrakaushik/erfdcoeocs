def rot(s):
    a=s[-1]+s[:len(s)-1]
    if a!=s:
        return a
    else :
        return rot(a)
t=int(input())
s=[]
a=[]
for _ in range(t):
    s.append(input())
for i in s:
    if len(set(i))==1:
        a.append('NO')
    else:
        a.append('YES')
        m=rot(i)
        a.append(m)

for i in a:
    print(i)
