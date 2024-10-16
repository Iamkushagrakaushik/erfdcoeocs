n=int(input())
for i in range(n):
    s=input()
    length=len(s)
    if length>10:
        print(s[0]+str(length-2)+s[-1])
    else:
        print(s)
        