n=int(input())
s=''
l=[' hate ',' love ','that ']
for i in range(1,n+1):
    s+='I'
    s+=l[(i+1)%2]
    if i<n:
        s+=l[2]
    else:
        s+='it'
print(s)     
    
     
     
     
     