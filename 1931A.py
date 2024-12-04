t=int(input())
s="abcdefghijklmnopqrstuvwxyz"
for _ in range(t):
    
    n=int(input())
    m=""
  
    if n>52:
        m+="z"
        n-=26
    if n>26:
        m+="z"
        n-=26

    if m=="":
        m="aa"+s[n-3]
    elif len(m)==1:
        if (n-2)>=0:
            m+="a"+s[n-2]
        else:
            m+="a"+s[n-2]
    else:
        m+=s[n-1]
    print("".join(sorted(m)))

    
