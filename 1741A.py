# def x(a):
#     c=1
#     for i in a:
#         if i=='X':
#             c+=1
#     return c
def s(a):
    s1=0
    if a=='M':
            s1=0
    elif a=='S':
        s1=-1
    else:
        s1=1
    return s1


t = int(input())
for _ in range(t):
    a,b=tuple(input().split())
    s1,s2=len(a),len(b)
    s1*=s(a[-1])
    s2*=s(b[-1])
    if s1>s2:
        print('>')
    elif s1<s2:
        print('<')
    else:
        print('=')
        
    