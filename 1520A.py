t=int(input())
a=[]
d={}
for _ in range(t):
    n=int(input())
    s=input()
    d={}
    if n==1:
        a.append("YES")
    else:
        for i in range(n-1):
            if s[i] not in d:
                d[s[i]]=1
            else:
                if i>1 and s[i-1]!=s[i] and d[s[i]]>0:
                    a.append("NO")
                    break
            d[s[i]]+=1
        else:
            a.append("YES")

            
    
for i in a:
    print(i)



