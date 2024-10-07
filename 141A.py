a=list(input())
 
a+=list(input())
a.sort()
 
c=list(input())
c.sort()
if c==a:
    print("YES")
else:
    print("NO")