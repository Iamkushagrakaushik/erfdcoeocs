def ev(n):
    s='0'
    for i in range(1,len(n)+1,1):
        s=str(eval(n[:i]+"+"+s))
    return s
        
n=int(input())
a=[]
for _ in range(n):
    m=int(input())
    s=input()
    a.append(ev(s.lstrip('0')))
for i in a:
    print(i)