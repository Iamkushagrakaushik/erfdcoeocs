n=int(input())
a=list(map(int,input().split()))
s,d=0,0
m=0
while m<n:
    if m%2==0:
        if a[0]>a[-1]:
            s+=a.pop(0)
            
        else:
            s+=a.pop(-1)
    else:
        if a[0]>a[-1]:
            d+=a.pop(0)
            
        else:
            d+=a.pop(-1)
    m+=1
print(s,d,sep=" ")




