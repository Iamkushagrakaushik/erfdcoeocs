t=int(input())
for _ in range(t):
    a=96
    n=int(input())
    s=input()
    i=n-1
    c=""
    while i>=0:
        if s[i]=='0':
            c+=chr(int(s[i-2]+s[i-1])+a)
            i-=2
        else :
            c+=chr(int(s[i])+a)
        i-=1
    
    print(c[::-1])

