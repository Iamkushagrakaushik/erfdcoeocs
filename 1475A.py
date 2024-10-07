t=int(input())
a=[]
for _ in range(t):
    x=int(input())
    if (x and (not(x & (x - 1))) ):
        a.append("NO")
    else:
        a.append("YES")

        

for h in a:
    print(h)
