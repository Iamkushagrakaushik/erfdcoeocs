k=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
if k==0:
    print(0)
else:
    s,c=0,0
    for i in a:
        s+=i
        if s<k:
            c+=1
        else:
            print(c+1)
            break
    else:
        print(-1)
