t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if (b+c)<(a-1):
        print(2*(b+c)+1)
    else:
        print(a*2-1)