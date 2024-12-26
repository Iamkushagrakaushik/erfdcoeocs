def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        total = sum(a)
        if total % n != 0:
            print("NO")
            continue
        
        target = total // n
        surplus = 0
        possible = True
        
        for i in range(n - 1):
            surplus += a[i] - target
            if surplus < 0:
                possible = False
                break
        
        print("YES" if possible else "NO")

# Run the solve function to handle input/output
solve()
