t=int(input())
for _ in range(t):
    s1=input()
    s2=input()
    i,c=0,0
    a,b=len(s1),len(s2)
    while i<min(a,b) and s1[i]==s2[i]:
        i+=1
    if i>0:
        print(a+b-i+1)
    else:
        print(a+b)