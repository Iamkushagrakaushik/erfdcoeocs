t=int(input())
for _ in range(t):
    s=input()
    o=s[1]
    x=int(s[0])
    y=int(s[2])
    if x>y:
        o=">"
    elif x<y:
        o="<"
    else:
        o="="
    print(s[0]+o+s[2])


    """if o=='=':
        if s[0]==s[2]:
            print(s)
        else:
            print(s[0]+o+s[0])
    elif o=='<':
        if int(s[0])<int(s[2]):
            print(s)
        elif s[0]==s[2]:
            print(s[0]+"="+s[0])
        else:
             print(s[0]+">"+s[2])
    else:
        if int(s[0])>int(s[2]):
            print(s)
        elif s[0]==s[2]:
            print(s[0]+"="+s[0])
        else:
             print(s[0]+"<"+s[2])"""


