t=int(input())
for _ in range(t):
    s=input()
    a=s.count('A')
    b=s.count('B')
    c=s.count('C')
    if a+c==b:
        print("YES")
    else:
        print("NO")