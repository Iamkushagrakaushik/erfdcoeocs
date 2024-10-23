t=int(input())
for _ in range(t):
    s=input()
    c=" "
    for i in s:
        if (c==" " or (c=='e' and i=='s') or (c=='Y' and i=='e')  or (c=='s' and i=='Y')) and i in "Yes":
            c=i
        else:
            print("NO")
            break
    else :
        print("YES") 