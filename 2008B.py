import math

def is_square_beautiful_matrix(n, s):
    k = int(math.isqrt(n))
    if k * k != n:
        return "No"
    
    # Length of the side of the square matrix
    side = k
    if s.count('0')!=(n-4*k+4):
        return "NO"
    
    # Check the first and last row
    if s[:side] != '1' * side or s[-side:] != '1' * side:
        return "No"
    
    # Check the first and last columns of the middle rows
    for i in range(1, side - 1):
        if s[i * side] != '1' or s[(i + 1) * side - 1] != '1':
            return "No"
    
    return "Yes"

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(is_square_beautiful_matrix(n, s))
