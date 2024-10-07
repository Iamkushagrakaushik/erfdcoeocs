n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
i=0
while(i<n):
    if sum(a[0:i])>sum(a[i:n]):
        break
    i+=1
print(i)