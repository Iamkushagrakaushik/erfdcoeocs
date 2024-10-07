t=int(input())
x=['a','b','c','d','e','f','g','h']
for _ in range(t):
    se=set()
    m=input()
    s=m[0]
    c=(m[1])
    for i in range(1,9):
        se.add(s+str(i))
    for i in x:
        se.add(i+c)
    se.remove(m)
    for i in se:
        print(i)
