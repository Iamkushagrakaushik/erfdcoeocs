t = int(input())
for _ in range(t):
    s=input()
    l=len(s)//2
    if len(s)<4:
        print("NO")
        continue
    for i in range(l-1):
        if s[i]!=s[i+1]:
            print("YES")
            break
    else:
        print("NO")
