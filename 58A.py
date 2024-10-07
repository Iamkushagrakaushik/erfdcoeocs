s=input().lower()
k='hello'
d=0
for i in s:
    if i==k[d]:
        d+=1
    if d>=5:
        print('YES')
        break
else:
    print('NO')        
