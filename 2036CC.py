t = int(input())
for _ in range(t):
    s = list(input())
    n = len(s)
    q = int(input())
    
    def h(i):
        if i >= 0 and i + 3 < n and s[i:i + 4] == ['1', '1', '0', '0']:
            return True
        else:
            return False
    
    c = 0
    for i in range(n - 3):
        if h(i):
            c += 1
    
    for __ in range(q):
        a, b = map(int, input().split())
        a -= 1
        o = s[a]
        
        if o == str(b):
            if c > 0:
                print("YES")
            else:
                print("NO")
            continue
        
        for i in range(a - 3, a + 1):
            if h(i):
                c -= 1
        
        s[a] = str(b)
        
        for i in range(a - 3, a + 1):
            if h(i):
                c += 1

        if c > 0:
            print("YES")
        else:
            print("NO")
