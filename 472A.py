def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return True
    if n <= 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False

n=int(input())
for i in range(3,n):
    if is_prime(i) and is_prime(n-i):
        print(i,n-i,sep=" ")
        break
