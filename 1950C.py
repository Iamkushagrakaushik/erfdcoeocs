t=int(input())
for _ in range(t):
    a,b=tuple(input().split(':'))
    x,y,z="","",""
    if a=="00":
        x="12"
        z=" AM"
    elif int(a)<12:
        x=a
        z=" AM"
    elif a=="12":
        x=a
        z=" PM"
    else:
        n=(int(a))%12
        z=" PM"
        if n<10:
            x="0"+str(n)
        else:
            x=str(n)
    print(x+":"+b+z)

    