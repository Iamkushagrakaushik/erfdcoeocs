n=int(input())
e=0
o=0
s=list(map(int,input().split()))
for i in range(3):
    if s[i]%2==0:
        e+=1
    else:
        o+=1
if e<o:
    for i in range(len(s)):
        if s[i]%2==0:
            print(i+1)
            break
else:
    for i in range(len(s)):
        if s[i]%2==1:
            print(i+1)
            break


        