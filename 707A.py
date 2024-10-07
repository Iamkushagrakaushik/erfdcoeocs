n,m=tuple(map(int,input().split()))
a=[]
c=0
for _ in range(n):
    a+=input().split()
for i in a:
    if i=='C' or i=='M' or i=='Y':
        print("#Color")
        break
else:
    print("#Black&White")