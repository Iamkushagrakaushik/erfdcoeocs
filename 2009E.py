def minimum_x(n, k):
    # Calculate the minimum x based on the parity of n
    if n % 2 == 0:
        # If n is even
        return (n // 2) * (2 * k + n - 1) % 2
    else:
        # If n is odd
        return (n % 2) * (2 * k + n - 1) % 2

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(minimum_x(n, k))
