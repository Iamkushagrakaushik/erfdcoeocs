n=int(input())
l=[]
t=0
for _ in range(n):
    a=input().split('|')
    if t==0:
        if a[0]=="OO":
            a[0]="++"

            t=1
        elif a[1]=="OO":
            t=1
            a[1]="++"
    l.append(a)
if t:
    print("YES")
    for i in l:
        print(i[0]+"|"+i[1])
else:
    print("NO")


     
