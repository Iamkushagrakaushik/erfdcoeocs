t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    j=n-1
    a=n
    for i in range(a//2):
        if s[i]!=s[j-i]:
            n-=2
        else:
            break
    print(n)


