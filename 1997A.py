t=int(input())
a=[]
for _ in range(t):
    s=input()
    n=len(s)
    if n==1 :
        if s!='z':
            m=ord(s)
            c=s+chr(m+1)
        else:
            c=s+'a'
    else:
        c=s
        for i in range(n-1):
            if s[i]==s[i+1]:
                if s[i]!='z':
                    m=ord(s[i])
                    c=s[:i+1]+chr(m+1)+ s[i+1:]
                else:
                    c=s[:i+1]+'a'+ s[i+1:]
                break
        else:
            if s[-1]!='z':
                    m=ord(s[-1])
                    c=s+chr(m+1)
            else:
                c=s+'a'
            
    a.append(c)
for i in a:
    print(i)
                
