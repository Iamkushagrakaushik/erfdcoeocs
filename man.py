t=int(input())
x=[]
for _ in range(t):
    a=""
    n,m=tuple(map(int,input().split()))
    for l in range(n):
        a+=input()
    c=a.count('#')
    o=(c//2 )+1
    k=0
    j=0
    if len(a)==1:
        x.append((1,1))
        continue
    for i in range(n*m):
        if a[i]=='#':
            k+=1
        if k==o:
            j=i+1
            
            break
    x.append((j//n,j%m))
for q,w in x:
    print(q,w,sep=" ")
"""def find_manhattan_center(t, test_cases):
    results = []
    for case in test_cases:
        n, m, grid = case
        coordinates = []

        # Collect all '#' coordinates
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '#':
                    coordinates.append((i + 1, j + 1))
        
        # Separate x and y coordinates
        x_coords = sorted([x for x, y in coordinates])
        y_coords = sorted([y for x, y in coordinates])
        
        # Find the median of the coordinates
        x_median = x_coords[len(x_coords) // 2]
        y_median = y_coords[len(y_coords) // 2]
        
        results.append((x_median, y_median))
    
    return results

# Example usage:
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    test_cases.append((n, m, grid))

results = find_manhattan_center(t, test_cases)
for result in results:
    print(result[0], result[1])"""



