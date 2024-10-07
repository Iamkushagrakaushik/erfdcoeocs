t = int(input())
for _ in range(t):
    x = int(input())
    a = list(map(int, input().split()))
    
    c = x
    o = False
    for _ in range(3):
        if a[c - 1] == 0:
            break
        c = a[c - 1]
    else:
        o= True

    if o:
        print("YES")
    else:
        print("NO")utkdmfgjnmrfjxgt::
