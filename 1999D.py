t=int(input())
for _ in range(t):
    a=input()
    s=input()
    if len(a)<len(s):
        print("NO")
        continue
    i,j=0,0
    c=""
    while i<len(a) and j< len(s):
        if a[i]==s[j]:
            c+=a[i]
            i+=1
            j+=1
        elif a[i]=='?' and i>=len(s):
            c+='a'
            i+=1
        elif a[i]=='?' :
            c+=s[i]
            i+=1
        else:
            i+=1
    if j==len(s)-1:
        print("YES")
        print(c)
    else:
        print("NO")