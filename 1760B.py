t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    c=ord('a')
    for i in s:
        if i=='z':
            c=ord('z')
            break
        elif ord(i)>c:
            c=ord(i)
    print(c-ord('a')+1)