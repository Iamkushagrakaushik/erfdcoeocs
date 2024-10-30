def get_anti_diagonals(matrix, n):
    diagonals = []

    for start_col in range(n):
        diagonal = []
        row, col = 0, start_col
        while row < n and col < n:
            diagonal.append(matrix[row][col])
            row += 1
            col += 1
        diagonals.append(diagonal)
    
     
    for start_row in range(1, n):
        diagonal = []
        row, col = start_row, 0
        while row < n and col < n:
            diagonal.append(matrix[row][col])
            row += 1
            col += 1
        diagonals.append(diagonal)
    
    return diagonals
def get_main_diagonals(matrix, n):
    diagonals = []
    
    # Upper part diagonals (including main diagonal)
    for start_col in range(n):
        diagonal = []
        row, col = 0, start_col
        while col >= 0 and row < n:
            diagonal.append(matrix[row][col])
            row += 1
            col -= 1
        diagonals.append(diagonal)

    # Lower part diagonals (below main diagonal)
    for start_row in range(1, n):
        diagonal = []
        row, col = start_row, n - 1
        while row < n and col >= 0:
            diagonal.append(matrix[row][col])
            row += 1
            col -= 1
        diagonals.append(diagonal)
    
    return diagonals

t=int(input())
for _ in range(t):
    n=int(input())
    a=[]
    for _ in range(n):
        l=list(map(int,input().split()))
        a.append(l)
    x=[0 for _ in range(2*n-1)]
    g,h=0,0
    p,q=get_anti_diagonals(a,n),get_main_diagonals(a,n)
    for i in range(2*n-1):
        c=min(p[i])
        if c<0:
            g-=c
        d=min(q[i])
        if d<0:
            h-=g

    print(max(g,h))        

