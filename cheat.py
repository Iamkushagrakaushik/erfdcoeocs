t = int(input())
results = []

for _ in range(t):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]
    
    # Collect coordinates of all `#` characters
    rows = []
    cols = []
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                rows.append(i + 1)
                cols.append(j + 1)
    
    # Find median of the rows and columns
    rows.sort()
    cols.sort()
    
    center_row = rows[len(rows) // 2]
    center_col = cols[len(cols) // 2]
    
    results.append((center_row, center_col))

for center in results:
    print(center[0], center[1])
