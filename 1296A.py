def can_make_odd_sum(t, test_cases):
    results = []
    
    for i in range(t):
        n = test_cases[i][0]
        a = test_cases[i][1]
        
        # Check if the sum is already odd
        if sum(a) % 2 == 1:
            results.append("YES")
            continue
        
        # Check for at least one odd and one even number
        has_odd = any(x % 2 == 1 for x in a)
        has_even = any(x % 2 == 0 for x in a)
        
        if has_odd and has_even:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Input reading
t = int(input())  # Number of test cases
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

# Process and output results
results = can_make_odd_sum(t, test_cases)
for res in results:
    print(res)