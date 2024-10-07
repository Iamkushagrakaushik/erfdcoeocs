import math

def max_good_array_length(l, r):
    max_diff = r - l
    k = int((math.sqrt(1 + 8 * max_diff) - 1) // 2)
    return k + 1

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    print(max_good_array_length(l, r))
